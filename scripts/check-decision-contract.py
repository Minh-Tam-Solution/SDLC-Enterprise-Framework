#!/usr/bin/env python3
"""Rule DEC-1: a model judgment that code consumes is a typed decision with an explicit abstain.

A decision function (routing, gating, classification) is declared in a `*.decision.json` file:

  {"decision_class": "<id>", "type": "choice", "layer": "REVIEW" | "ADVISORY",
   "options": {"<option>": "<what it means>", ..., "insufficient_evidence": "<when to choose it>"},
   "cases": [{"name": "empty-state", "state": "", "expect": "insufficient_evidence"},
             {"name": "<positive control>", "state": "<input>", "expect": "<another option>"}]}

A declaration has a defect when (definition, not examples):
  - `type` is not `choice`: a yes/no or score question has no abstain slot, so empty input returns
    the value that means "safe" (fail-open);
  - `options` lacks `insufficient_evidence`, or has no other option;
  - `layer` is not REVIEW or ADVISORY: a probabilistic function is never MACHINE;
  - no case with an empty `state` expecting `insufficient_evidence` (the acceptance case), or no case
    with a non-empty `state` expecting another option (the positive control), or an `expect` that is
    not an option.
With --run CMD each case is also run: CMD gets the state on stdin (DECISION_CLASS in its environment)
and prints one option as its last stdout line. Output that is not an option (prose) or differs from
`expect` is a defect. CMD exiting non-zero, or an unreadable declaration, is "cannot measure".

Burn case: a hosted typed-decision service given an EMPTY state chose a content class at confidence
0.70; adding `insufficient_evidence` as an option made it abstain at 1.0 with the positive control
unchanged. Its yes/no form returned 0.08 ("not sensitive") on empty input. Contract:
ai-engineering/context-and-hats.md, "Decisions code consumes".

Files: positional paths, or every tracked `*.decision.json` under --root (default .).
Counts declarations with a defect; --enforce turns count > 0 red (exit 2).
Exit codes (controls/rule-contract.md): 0 pass, 1 cannot measure, 2 violation. Last stdout line is the label.
"""
import json, os, shlex, subprocess, sys, tempfile

GATE = "check-decision-contract"
ABSTAIN = "insufficient_evidence"
FIX = "make_each_RED_line_above_hold"


def label(result, reason, fix=""):
    print(f"result={result} gate={GATE} reason={reason}" + (f" fix={fix}" if fix else ""))


def unmeasurable(msg, reason):
    print(msg, file=sys.stderr)
    label("insufficient_evidence", reason)
    sys.exit(1)


def defects(spec, run):
    """Return the list of defects of one declaration; raise RuntimeError when it cannot be measured."""
    out = []
    if not isinstance(spec, dict):
        raise RuntimeError("declaration is not a JSON object")
    if spec.get("type") != "choice":
        out.append(f"type={spec.get('type')!r}: only `choice` has an abstain slot")
    opts = spec.get("options")
    opts = opts if isinstance(opts, dict) else {}
    if ABSTAIN not in opts:
        out.append(f"options lack {ABSTAIN}")
    if not [o for o in opts if o != ABSTAIN]:
        out.append("no option besides insufficient_evidence")
    if spec.get("layer") not in ("REVIEW", "ADVISORY"):
        out.append(f"layer={spec.get('layer')!r}: a probabilistic decision is REVIEW or ADVISORY, never MACHINE")
    cases = [c for c in spec.get("cases") or [] if isinstance(c, dict)]
    if not any(str(c.get("state", "x")).strip() == "" and c.get("expect") == ABSTAIN for c in cases):
        out.append("no acceptance case: empty state must expect insufficient_evidence")
    if not any(str(c.get("state", "")).strip() and c.get("expect") not in (None, ABSTAIN) for c in cases):
        out.append("no positive control: a non-empty state expecting another option")
    out += [f"case {c.get('name')!r}: expect {c.get('expect')!r} is not an option" for c in cases if c.get("expect") not in opts]
    if run:
        env = dict(os.environ, DECISION_CLASS=str(spec.get("decision_class", "")))
        for c in cases:
            p = subprocess.run(shlex.split(run), input=str(c.get("state", "")), capture_output=True, text=True, env=env)
            if p.returncode != 0:
                raise RuntimeError(f"--run exited {p.returncode} on case {c.get('name')!r}: {p.stderr.strip()[-200:]}")
            lines = [l.strip() for l in p.stdout.splitlines() if l.strip()]
            got = lines[-1] if lines else ""
            if got not in opts:
                out.append(f"case {c.get('name')!r}: output {got[:60]!r} is not an option (never parse prose)")
            elif got != c.get("expect"):
                out.append(f"case {c.get('name')!r}: got {got!r}, want {c.get('expect')!r}")
    return out


def main(argv):
    root, run, enforce, files = ".", "", False, []
    it = iter(argv)
    for a in it:
        if a == "--root": root = next(it, "")
        elif a == "--run": run = next(it, "")
        elif a == "--enforce": enforce = True
        elif a == "--selftest": return selftest()
        elif a.startswith("--"): unmeasurable(f"unknown argument: {a}", "unknown_argument")
        else: files.append(a)
    if not files:
        p = subprocess.run(["git", "-C", root, "ls-files", "-z", "*.decision.json"], capture_output=True, text=True)
        if p.returncode != 0:
            unmeasurable(p.stderr.strip() or "git ls-files failed", "git_ls_files_failed")
        files = [os.path.join(root, f) for f in p.stdout.split("\0") if f]
    bad = 0
    for f in files:
        try:
            with open(f, encoding="utf-8") as fh:
                d = defects(json.load(fh), run)
        except (OSError, ValueError, RuntimeError) as e:
            unmeasurable(f"{f}: {e}", "unreadable_or_run_failed")
        if d:
            bad += 1
            print(f"RED — {f}: " + "; ".join(d))
        else:
            print(f"OK {f}")
    print(f"count={bad} files={len(files)}")
    if not files:
        label("pass", "no_decision_specs"); return 0
    if bad and enforce:
        label("violation", f"defective_{bad}", FIX); return 2
    label("pass", f"advisory_count_{bad}" if bad else "clean", FIX if bad else ""); return 0


def selftest():
    here = os.path.dirname(os.path.abspath(__file__))
    good = os.path.join(here, "fixtures", "pr-risk.decision.json")
    stub = "bash " + shlex.quote(os.path.join(here, "fixtures", "decide-pr-risk-stub.sh"))
    with tempfile.TemporaryDirectory() as t:
        def spec(name, **over):
            with open(good, encoding="utf-8") as fh:
                s = json.load(fh)
            s.update(over)
            s = {k: v for k, v in s.items() if v is not None}
            p = os.path.join(t, name)
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(s, fh)
            return p

        def rc(*args):
            return subprocess.run([sys.executable, __file__, *args], capture_output=True, text=True).returncode

        with open(good, encoding="utf-8") as fh:
            g = json.load(fh)
        no_abstain = {k: v for k, v in g["options"].items() if k != ABSTAIN}
        broken = os.path.join(t, "broken.decision.json")
        with open(broken, "w") as fh:
            fh.write("{not json")
        cases = [  # (name, want, args)
            ("green: the sample declaration", 0, [good, "--enforce"]),
            ("green: the sample run against its stub", 0, [good, "--enforce", "--run", stub]),
            ("red: fail-open function (case A2, confident answer on empty state)", 2, [good, "--enforce", "--run", "bash -c 'echo none'"]),
            ("red: prose output", 2, [good, "--enforce", "--run", "bash -c 'echo I think this touches a migration'"]),
            ("red: no insufficient_evidence option", 2, [spec("a.json", options=no_abstain, cases=[g["cases"][1]]), "--enforce"]),
            ("red: yes/no type at MACHINE", 2, [spec("b.json", type="noul", layer="MACHINE"), "--enforce"]),
            ("red: no positive control", 2, [spec("c.json", cases=[g["cases"][0]]), "--enforce"]),
            ("advisory: defect counted, not blocked", 0, [spec("d.json", layer="MACHINE")]),
            ("cannot measure: unreadable declaration", 1, [broken]),
            ("cannot measure: decision function crashes", 1, [good, "--run", "bash -c 'exit 3'"]),
        ]
        fails = [f"{n}: got {r}, want {w}" for n, w, a in cases for r in [rc(*a)] if r != w]
    if fails:
        print("selftest BROKEN:\n  " + "\n  ".join(fails))
        label("insufficient_evidence", "selftest_broken"); return 1  # broken gate = cannot measure
    print(f"selftest OK ({len(cases)} cases)")
    label("pass", "selftest_ok"); return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
