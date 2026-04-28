/* global React, Brandmark, Icon */
/* ============================================================
   SDLC Framework — landing components
   ============================================================ */
const { useState: useStateS, useEffect: useEffectS } = React;

/* ---------- SDLC brand mark (different from Endiorbot) ---------- */
function SdlcBrand({ size = 28 }) {
  return (
    <span className="brandmark">
      <span className="brand-glyph" style={{ width: size, height: size }}>
        <svg viewBox="0 0 32 32" width={size} height={size} aria-hidden="true">
          <defs>
            <linearGradient id="sbg" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="var(--accent-2)" />
              <stop offset="100%" stopColor="var(--accent)" />
            </linearGradient>
          </defs>
          {[0,1,2,3,4,5,6].map(i => {
            const a = (i / 7) * Math.PI * 2 - Math.PI / 2;
            const r = 10;
            const cx = 16 + Math.cos(a) * r;
            const cy = 16 + Math.sin(a) * r;
            return <circle key={i} cx={cx} cy={cy} r="2.2" fill="url(#sbg)" />;
          })}
          <circle cx="16" cy="16" r="2.6" fill="none" stroke="var(--ink)" strokeWidth="1.2" />
        </svg>
      </span>
      <span className="brand-name">SDLC<span className="dot-orbit"> · </span>Framework</span>
    </span>
  );
}

/* ---------- Top nav ---------- */
function SdlcNav({ t, lang, setLang }) {
  return (
    <nav className="nav">
      <div className="shell nav-inner">
        <a href="#top" aria-label="SDLC Framework"><SdlcBrand /></a>
        <div className="nav-links">
          <a href="#pillars">{t.nav.framework}</a>
          <a href="#stages">Stages</a>
          <a href="#tiers">Tiers</a>
          <a href="#souls">Roles</a>
          <a href="#refs">{t.nav.endiorbot}</a>
          <a href="#adopt">Adopt</a>
        </div>
        <div className="nav-actions">
          <div className="lang" role="group" aria-label="language">
            <button aria-pressed={lang === "en"} onClick={() => setLang("en")}>EN</button>
            <button aria-pressed={lang === "vi"} onClick={() => setLang("vi")}>VI</button>
          </div>
          <a href="#" className="btn btn-ghost" style={{ padding: "8px 14px" }}>
            <Icon.Github />
            <span style={{ fontSize: 12, fontFamily: "var(--font-mono)" }}>sdlc/framework</span>
          </a>
        </div>
      </div>
    </nav>
  );
}

/* ---------- Hero ---------- */
function SdlcHero({ t }) {
  const stats = [t.hero.stat1, t.hero.stat2, t.hero.stat3, t.hero.stat4, t.hero.stat5];
  return (
    <section className="hero" id="top">
      <div className="shell">
        <div className="hero-meta">
          <span className="pill"><span className="live" />{t.hero.eyebrow}</span>
        </div>
        <h1 className="display" style={{ marginBottom: 28, maxWidth: "16ch" }}>
          {t.hero.headline_a}{" "}<em>{t.hero.headline_em}</em>{" "}{t.hero.headline_b}
        </h1>
        <p className="hero-sub" style={{ maxWidth: "62ch" }}>{t.hero.sub}</p>
        <div className="hero-cta">
          <a href="#pillars" className="btn btn-primary">{t.hero.ctaPrimary}<Icon.Arrow /></a>
          <a href="#refs" className="btn btn-ghost">{t.hero.ctaSecondary}</a>
        </div>
        <div className="hero-strip" role="list">
          {stats.map((s, i) => (
            <div key={i} role="listitem">
              <div className="num">{i === 0 ? <span className="accent">{s.n}</span> : s.n}</div>
              <div className="lbl">{s.l}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Promise ---------- */
function PromiseSection({ t }) {
  return (
    <section className="section-divider" id="promise">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.promise.eyebrow}</div>
          <h2 className="section-h">{t.promise.title}</h2>
        </div>
        <p style={{ fontSize: "clamp(18px, 1.7vw, 24px)", color: "var(--ink-2)", maxWidth: "70ch", lineHeight: 1.55, textWrap: "pretty" }}>
          {t.promise.body}
        </p>
      </div>
    </section>
  );
}

/* ---------- Seven pillars ---------- */
function PillarsSection({ t }) {
  return (
    <section className="section-divider" id="pillars">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.pillars.eyebrow}</div>
          <h2 className="section-h">{t.pillars.title}</h2>
          <p className="lede">{t.pillars.sub}</p>
        </div>
        <div className="pillars-grid">
          {t.pillars.items.map((p, i) => (
            <div className="pillar-card" key={i}>
              <div className="num">{p.n}</div>
              <h4>{p.t}</h4>
              <p>{p.d}</p>
            </div>
          ))}
          <div className="pillar-card p7">
            <div className="num">{t.pillars.sec7.n}</div>
            <h4>{t.pillars.sec7.t}</h4>
            <p>{t.pillars.sec7.d}</p>
          </div>
          <div className="pillar-card p7" style={{ gridColumn: "span 2" }}>
            <div className="num">{t.pillars.sec8.n}</div>
            <h4>{t.pillars.sec8.t}</h4>
            <p>{t.pillars.sec8.d}</p>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ---------- 10-Stage timeline (interactive) ---------- */
function StagesSection({ t }) {
  const [sel, setSel] = useStateS(0);
  const stage = t.stages.data[sel];
  return (
    <section className="section-divider" id="stages">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.stages.eyebrow}</div>
          <h2 className="section-h">{t.stages.title}</h2>
          <p className="lede">{t.stages.sub}</p>
        </div>
        <div className="stages-timeline" role="tablist">
          {t.stages.data.map((s, i) => (
            <div key={i} className="stage-cell"
                 role="tab" tabIndex={0}
                 aria-selected={i === sel}
                 onClick={() => setSel(i)}
                 onKeyDown={(e) => { if (e.key === "Enter" || e.key === " ") setSel(i); }}>
              <div className="sid">{s.id}</div>
              <div className="sname">{s.name}</div>
              <div className="sgate">{s.q}</div>
            </div>
          ))}
        </div>
        <div className="stage-detail">
          <div>
            <h3 style={{ marginBottom: 14 }}>{stage.id} · {stage.name}</h3>
            <div className="meta">
              <span><strong>Gate:</strong> {stage.gate}</span>
              <span><strong>Reqs:</strong> {stage.reqs}</span>
              <span><strong>Parallel:</strong> {stage.parallel}</span>
            </div>
          </div>
          <ul>
            {stage.deliverables.map((d, i) => (
              <li key={i}><span className="k">{d[0]}</span><span>{d[1]}</span></li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}

/* ---------- Four tiers ---------- */
function TiersSection({ t }) {
  return (
    <section className="section-divider" id="tiers">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.tiers.eyebrow}</div>
          <h2 className="section-h">{t.tiers.title}</h2>
          <p className="lede">{t.tiers.sub}</p>
        </div>
        <div className="tiers-grid">
          {t.tiers.items.map((tier, i) => (
            <div className="tier-card" key={i} data-rec={tier.rec}>
              <div className="lvl">{tier.lvl}</div>
              <h4>{tier.name}</h4>
              <div className="who">{tier.who}</div>
              <div className="num"><em>Stages:</em> {tier.stages}</div>
              <ul>
                {tier.features.map((f, j) => <li key={j}>{f}</li>)}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Quality gates ---------- */
function GatesSection({ t }) {
  return (
    <section className="section-divider" id="gates">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.gates.eyebrow}</div>
          <h2 className="section-h">{t.gates.title}</h2>
          <p className="lede">{t.gates.sub}</p>
        </div>
        <div className="gates" style={{ padding: 0 }}>
          {t.gates.items.map((g, i) => (
            <div key={i} style={{
              display: "grid",
              gridTemplateColumns: "80px 1fr 1.6fr",
              gap: 24, alignItems: "center",
              padding: "22px 28px",
              borderTop: i === 0 ? 0 : "1px solid var(--line)"
            }}>
              <div style={{
                fontFamily: "var(--font-display)",
                fontSize: 36, color: "var(--accent)", letterSpacing: "-0.02em"
              }}>{g.id}</div>
              <div>
                <div style={{ fontFamily: "var(--font-mono)", fontSize: 11, letterSpacing: "0.08em", color: "var(--ink-3)", textTransform: "uppercase" }}>{g.phase}</div>
                <div style={{ fontFamily: "var(--font-display)", fontSize: 22, color: "var(--ink)", letterSpacing: "-0.02em", marginTop: 4 }}>{g.title}</div>
              </div>
              <ul style={{ listStyle: "none", padding: 0, margin: 0, display: "flex", flexDirection: "column", gap: 6 }}>
                {g.ev.map((e, j) => (
                  <li key={j} style={{ fontSize: 13.5, color: "var(--ink-2)", display: "flex", gap: 10 }}>
                    <span style={{ color: "var(--accent)", fontFamily: "var(--font-mono)" }}>✓</span>{e}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Vibecoding meter ---------- */
function VibeSection({ t }) {
  return (
    <section className="section-divider" id="vibe">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.vibe.eyebrow}</div>
          <h2 className="section-h">{t.vibe.title}</h2>
          <p className="lede">{t.vibe.body}</p>
        </div>
        <div className="vibe-wrap">
          <div className="vibe-meter">
            <h4>Signal weights</h4>
            {t.vibe.signals.map((s, i) => (
              <div key={i} className="row"><span>{s.l}</span><span>{s.w}</span></div>
            ))}
          </div>
          <div className="vibe-meter">
            <h4>Routing</h4>
            <div className="scale" style={{ marginTop: 14 }}>
              <i className="a" /><i className="b" /><i className="c" /><i className="d" />
            </div>
            <div className="ticks">
              <span>0</span><span>20</span><span>40</span><span>60</span><span>100</span>
            </div>
            <div style={{ marginTop: 18 }}>
              {t.vibe.routing.map((r, i) => (
                <div key={i} className="row">
                  <span><strong style={{ color: "var(--ink)", marginRight: 10 }}>{r.range}</strong>{r.label}</span>
                  <span>{r.action}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ---------- 18 SOULs ---------- */
function SoulsSection({ t }) {
  return (
    <section className="section-divider" id="souls">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.souls.eyebrow}</div>
          <h2 className="section-h">{t.souls.title}</h2>
          <p className="lede">{t.souls.sub}</p>
        </div>
        <div className="agents-legend" style={{ marginBottom: 20 }}>
          {t.souls.tiers.map((tier, i) => (
            <span key={i}>
              <i style={{
                background: tier.c === "advisor" ? "var(--violet)" :
                           tier.c === "executor" ? "var(--accent)" : "var(--ink-3)"
              }} />{tier.l}
            </span>
          ))}
        </div>
        <div className="souls-grid">
          {t.souls.items.map((s, i) => (
            <div key={i} className={`soul-cell ${s.c}`}>
              <div className="role">{s.role}</div>
              <div className="name">@{s.name}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Training modules ---------- */
function TrainingSection({ t }) {
  return (
    <section className="section-divider" id="training">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.training.eyebrow}</div>
          <h2 className="section-h">{t.training.title}</h2>
          <p className="lede">{t.training.sub}</p>
        </div>
        <div className="modules-list">
          {t.training.items.map((m, i) => (
            <div className="module-row" key={i}>
              <div className="midx">M{m.i}</div>
              <div className="mtitle">{m.t}<small>{m.sub}</small></div>
              <div className="mhrs">{m.h}</div>
              <div className="mtier">{m.tier}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Reference implementations ---------- */
function RefsSection({ t }) {
  const r = t.refs;
  return (
    <section className="section-divider" id="refs">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{r.eyebrow}</div>
          <h2 className="section-h">{r.title}</h2>
          <p className="lede">{r.sub}</p>
        </div>
        <div className="refs-grid">
          <div className="ref-card live">
            <div className="badge"><span className="live" />{r.endior.badge}</div>
            <h3>{r.endior.title}</h3>
            <p>{r.endior.body}</p>
            <div className="ctas">
              {r.endior.ctas.map((c, i) => (
                <a key={i} href={c[1]} className={i === 0 ? "btn btn-primary" : "btn btn-ghost"}>{c[0]}</a>
              ))}
            </div>
            <div className="stats">
              {r.endior.stats.map((s, i) => (
                <div key={i}><div className="num">{s[0]}</div><div className="lbl">{s[1]}</div></div>
              ))}
            </div>
          </div>
          <div className="ref-card">
            <div className="badge">{r.orch.badge}</div>
            <h3>{r.orch.title}</h3>
            <p>{r.orch.body}</p>
            <div className="ctas">
              {r.orch.ctas.map((c, i) => (
                <a key={i} href={c[1]} className={i === 0 ? "btn btn-primary" : "btn btn-ghost"}>{c[0]}</a>
              ))}
            </div>
            <div className="stats">
              {r.orch.stats.map((s, i) => (
                <div key={i}><div className="num">{s[0]}</div><div className="lbl">{s[1]}</div></div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

/* ---------- Adoption rail ---------- */
function AdoptSection({ t }) {
  return (
    <section className="section-divider" id="adopt">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.adopt.eyebrow}</div>
          <h2 className="section-h">{t.adopt.title}</h2>
          <p className="lede">{t.adopt.sub}</p>
        </div>
        <div className="adopt-rail">
          {t.adopt.steps.map((s, i) => (
            <div className="adopt-step" key={i}>
              <div className="day">{s.day}</div>
              <div className="num">{s.num}</div>
              <h4>{s.t}</h4>
              <p>{s.d}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Standards ---------- */
function StandardsSection({ t }) {
  return (
    <section className="section-divider" id="standards">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.standards.eyebrow}</div>
          <h2 className="section-h">{t.standards.title}</h2>
          <p className="lede">{t.standards.sub}</p>
        </div>
        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: 12,
        }}>
          {t.standards.items.map((it, i) => (
            <div key={i} style={{
              background: "var(--bg-1)",
              border: "1px solid var(--line)",
              borderRadius: 12,
              padding: "20px 22px",
              minHeight: 110,
              display: "flex", flexDirection: "column", gap: 6
            }}>
              <div style={{
                fontFamily: "var(--font-mono)",
                fontSize: 12,
                color: "var(--accent)",
                letterSpacing: "0.04em"
              }}>{it[0]}</div>
              <div style={{ fontSize: 13, color: "var(--ink-2)", lineHeight: 1.5 }}>{it[1]}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- FAQ ---------- */
function FaqSdlc({ t }) {
  const [open, setOpen] = useStateS(0);
  return (
    <section className="section-divider" id="faq">
      <div className="shell">
        <div className="section-head">
          <div className="eyebrow"><span className="dot" />{t.faq.eyebrow}</div>
          <h2 className="section-h">{t.faq.title}</h2>
        </div>
        <div className="faq-wrap">
          {t.faq.items.map((it, i) => (
            <div key={i} className="faq-item" data-open={i === open}>
              <button className="faq-q" onClick={() => setOpen(i === open ? -1 : i)}>
                <span>{it.q}</span><span className="marker">+</span>
              </button>
              <div className="faq-a"><p style={{ margin: 0 }}>{it.a}</p></div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

/* ---------- Footer ---------- */
function FootSdlc({ t }) {
  return (
    <footer className="foot">
      <div className="shell">
        <div className="foot-grid">
          <div>
            <SdlcBrand />
            <p className="foot-tag" style={{ marginTop: 14 }}>
              <strong style={{ color: "var(--ink-2)" }}>{t.footer.tag}</strong><br />
              {t.footer.sub}
            </p>
          </div>
          {t.footer.cols.map((c, i) => (
            <div className="foot-col" key={i}>
              <h5>{c.t}</h5>
              <ul>
                {c.links.map((l, j) => <li key={j}><a href={l[1]}>{l[0]}</a></li>)}
              </ul>
            </div>
          ))}
        </div>
        <div className="foot-bottom">
          <span>{t.footer.auth}</span>
          <span>v6.3.1 · MIT</span>
        </div>
      </div>
    </footer>
  );
}

Object.assign(window, {
  SdlcBrand, SdlcNav, SdlcHero, PromiseSection, PillarsSection, StagesSection,
  TiersSection, GatesSection, VibeSection, SoulsSection, TrainingSection,
  RefsSection, AdoptSection, StandardsSection, FaqSdlc, FootSdlc
});
