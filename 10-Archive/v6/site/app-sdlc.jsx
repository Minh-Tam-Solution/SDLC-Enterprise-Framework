/* global React, ReactDOM,
   SdlcNav, SdlcHero, PromiseSection, PillarsSection, StagesSection,
   TiersSection, GatesSection, VibeSection, SoulsSection, TrainingSection,
   RefsSection, AdoptSection, StandardsSection, FaqSdlc, FootSdlc,
   TweaksPanel, useTweaks, TweakSection, TweakRadio, TweakToggle */

const TWEAK_DEFAULTS_SDLC = /*EDITMODE-BEGIN*/{
  "theme": "rust",
  "density": "cozy",
  "showVibe": true,
  "showStandards": true,
  "showTraining": true
}/*EDITMODE-END*/;

function AppSdlc() {
  const [lang, setLang] = React.useState(() => localStorage.getItem("sdlc-lang") || "en");
  React.useEffect(() => {
    localStorage.setItem("sdlc-lang", lang);
    document.documentElement.lang = lang;
  }, [lang]);

  const [tweaks, setTweak] = useTweaks(TWEAK_DEFAULTS_SDLC);

  React.useEffect(() => {
    document.documentElement.dataset.theme = tweaks.theme;
    document.documentElement.dataset.density = tweaks.density;
    document.documentElement.dataset.site = "sdlc";
  }, [tweaks.theme, tweaks.density]);

  const t = window.sdlcCopy[lang];

  return (
    <>
      <SdlcNav t={t} lang={lang} setLang={setLang} />
      <SdlcHero t={t} />
      <PromiseSection t={t} />
      <PillarsSection t={t} />
      <StagesSection t={t} />
      <TiersSection t={t} />
      <GatesSection t={t} />
      {tweaks.showVibe && <VibeSection t={t} />}
      <SoulsSection t={t} />
      {tweaks.showTraining && <TrainingSection t={t} />}
      <RefsSection t={t} />
      <AdoptSection t={t} />
      {tweaks.showStandards && <StandardsSection t={t} />}
      <FaqSdlc t={t} />
      <FootSdlc t={t} />

      <TweaksPanel title="Tweaks">
        <TweakSection label="Theme">
          <TweakRadio
            label="Palette"
            value={tweaks.theme}
            onChange={(v) => setTweak("theme", v)}
            options={[
              { value: "rust", label: "Rust" },
              { value: "ink", label: "Ink" },
              { value: "cobalt", label: "Cobalt" },
              { value: "paper", label: "Paper" },
            ]}
          />
          <TweakRadio
            label="Density"
            value={tweaks.density}
            onChange={(v) => setTweak("density", v)}
            options={[
              { value: "cozy", label: "Cozy" },
              { value: "compact", label: "Compact" },
            ]}
          />
        </TweakSection>
        <TweakSection label="Sections">
          <TweakToggle label="Vibecoding meter" value={tweaks.showVibe} onChange={(v) => setTweak("showVibe", v)} />
          <TweakToggle label="Training modules" value={tweaks.showTraining} onChange={(v) => setTweak("showTraining", v)} />
          <TweakToggle label="Standards alignment" value={tweaks.showStandards} onChange={(v) => setTweak("showStandards", v)} />
        </TweakSection>
      </TweaksPanel>
    </>
  );
}

const rootSdlc = ReactDOM.createRoot(document.getElementById("root"));
rootSdlc.render(<AppSdlc />);
