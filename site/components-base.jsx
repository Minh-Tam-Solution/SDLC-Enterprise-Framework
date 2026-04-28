/* global React */
/* ============================================================
   Endiorbot — shared UI components (icons, brand, terminal)
   ============================================================ */
const { useState, useEffect, useRef, useMemo } = React;

/* ---------- Brandmark ---------- */
function Brandmark({ size = 28 }) {
  return (
    <span className="brandmark">
      <span className="brand-glyph" style={{ width: size, height: size }}>
        <svg viewBox="0 0 32 32" width={size} height={size} aria-hidden="true">
          <defs>
            <linearGradient id="ebg" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="var(--accent-2)" />
              <stop offset="100%" stopColor="var(--accent)" />
            </linearGradient>
          </defs>
          {/* outer orbit */}
          <ellipse cx="16" cy="16" rx="14" ry="6" fill="none" stroke="var(--ink-3)" strokeWidth="1" opacity="0.55" transform="rotate(-22 16 16)" />
          {/* inner E */}
          <path d="M9 9 H22 M9 16 H19 M9 23 H22" stroke="url(#ebg)" strokeWidth="2.4" strokeLinecap="round" fill="none" />
          {/* satellite dot */}
          <circle cx="27.4" cy="11.4" r="2.1" fill="url(#ebg)" />
        </svg>
      </span>
      <span className="brand-name">Endior<span className="dot-orbit">·</span>bot</span>
    </span>
  );
}

/* ---------- Channel icons (small, line) ---------- */
const Icon = {
  CLI: () => (
    <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <rect x="2.5" y="4.5" width="19" height="15" rx="2" /><path d="M6 9.5l3 2.5-3 2.5M11 15h6" />
    </svg>
  ),
  Web: () => (
    <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18" />
    </svg>
  ),
  Telegram: () => (
    <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 4 3 11l6 2 2 6 4-5 5 4 1-14z" /><path d="M9 13l9-7" />
    </svg>
  ),
  Zalo: () => (
    <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 6h16v10H8l-4 4V6z" /><path d="M8 11h2l-2 2h2M14 11l2 2 2-2M14 13v-2" />
    </svg>
  ),
  Desktop: () => (
    <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      <rect x="2.5" y="4" width="19" height="13" rx="1.5" /><path d="M9 21h6M12 17v4" />
    </svg>
  ),
  Github: () => (
    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 .3a12 12 0 0 0-3.79 23.4c.6.1.82-.26.82-.58v-2c-3.34.72-4.04-1.6-4.04-1.6-.55-1.39-1.34-1.76-1.34-1.76-1.09-.74.08-.73.08-.73 1.21.09 1.84 1.24 1.84 1.24 1.07 1.83 2.81 1.3 3.5 1 .1-.78.42-1.3.76-1.6-2.66-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.11-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.65 1.66.24 2.88.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.81 5.62-5.49 5.92.43.37.81 1.1.81 2.22v3.29c0 .32.22.7.83.58A12 12 0 0 0 12 .3"/></svg>
  ),
  Star: () => (
    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.9L12 18l-6.2 3.1L7 14.2 2 9.3l6.9-1z"/></svg>
  ),
  Arrow: () => (
    <svg className="arr" viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round"><path d="M3 8h10M9 4l4 4-4 4" /></svg>
  ),
};

/* ---------- Animated terminal ---------- */
function Terminal({ data, key }) {
  const [step, setStep] = useState(0);
  const [typed, setTyped] = useState("");
  const [phase, setPhase] = useState("typing"); // typing | output | wait
  const dataRef = useRef(data);
  useEffect(() => { dataRef.current = data; setStep(0); setTyped(""); setPhase("typing"); }, [data]);

  useEffect(() => {
    let cancelled = false;
    let timer;
    const lines = dataRef.current.lines;
    if (step >= lines.length) {
      // restart loop after pause
      timer = setTimeout(() => {
        if (!cancelled) { setStep(0); setTyped(""); setPhase("typing"); }
      }, 4000);
      return () => { cancelled = true; clearTimeout(timer); };
    }
    const line = lines[step];
    if (line.t === "prompt") {
      // type the cmd char by char
      const cmd = line.c || "";
      if (typed.length < cmd.length) {
        timer = setTimeout(() => setTyped(cmd.slice(0, typed.length + 1)), 28 + Math.random() * 30);
      } else {
        timer = setTimeout(() => { setStep(s => s + 1); setTyped(""); }, 480);
      }
    } else if (line.t === "spacer") {
      timer = setTimeout(() => setStep(s => s + 1), 80);
    } else {
      // output / comment / caret
      timer = setTimeout(() => setStep(s => s + 1), line.t === "caret" ? 1500 : 380);
    }
    return () => { cancelled = true; clearTimeout(timer); };
  }, [step, typed]);

  const lines = data.lines;
  return (
    <div className="terminal" role="img" aria-label="endiorbot terminal demo">
      <div className="terminal-bar">
        <div className="dots"><span /><span /><span /></div>
        <div className="title">{data.title}</div>
        <div style={{ width: 48 }} />
      </div>
      <div className="terminal-body">
        {lines.slice(0, step + 1).map((ln, i) => {
          const isCurrent = i === step;
          if (ln.t === "spacer") return <div key={i} className="line">&nbsp;</div>;
          if (ln.t === "caret") return <div key={i} className="line"><span className="prompt">$</span> <span className="caret" /></div>;
          if (ln.t === "comment") return <div key={i} className="line"><span className="comment">{ln.v}</span></div>;
          if (ln.t === "prompt") {
            const full = ln.c || "";
            const text = isCurrent ? typed : full;
            return (
              <div key={i} className="line">
                <span className="prompt">{ln.v}</span>{" "}
                <span dangerouslySetInnerHTML={{ __html: highlightCmd(text) }} />
                {isCurrent && typed.length < full.length && <span className="caret" />}
              </div>
            );
          }
          if (ln.t === "out") {
            return <div key={i} className="line"><span className="ok" dangerouslySetInnerHTML={{ __html: highlightOut(ln.v) }} /></div>;
          }
          return null;
        })}
      </div>
    </div>
  );
}

function highlightCmd(s) {
  // basic highlight: @agent, --flag, "strings"
  return escapeHtml(s)
    .replace(/(@[a-z]+)/g, '<span class="at-agent">$1</span>')
    .replace(/(--?[a-z][\w-]*)/g, '<span class="keyw">$1</span>');
}
function highlightOut(s) {
  return escapeHtml(s)
    .replace(/(@[a-z]+)/g, '<span class="at-agent">$1</span>');
}
function escapeHtml(s) { return s.replace(/[&<>]/g, m => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[m])); }

/* ---------- Install bar ---------- */
function InstallBar({ cmd }) {
  const [copied, setCopied] = useState(false);
  const onCopy = async () => {
    try {
      await navigator.clipboard.writeText(cmd);
      setCopied(true);
      setTimeout(() => setCopied(false), 1400);
    } catch {}
  };
  return (
    <div className="install" role="group" aria-label="install command">
      <span className="prompt">$</span>
      <span className="cmd">{cmd}</span>
      <button className={"copy" + (copied ? " copied" : "")} onClick={onCopy} aria-label="copy install command">
        {copied ? "COPIED" : "COPY"}
      </button>
    </div>
  );
}

Object.assign(window, { Brandmark, Icon, Terminal, InstallBar });
