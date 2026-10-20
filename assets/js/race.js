// V2: Tipp-vs-Sprich-Rennen. Simuliert dieselbe Mail bei ~40 vs. ~150 Wörtern/Min.
// Läuft 6× beschleunigt, die Uhr zeigt die simulierte Echtzeit.
(() => {
  const root = document.querySelector('[data-race]');
  if (!root) return;

  const TEXT = 'Hallo Frau Becker, vielen Dank für Ihre schnelle Rückmeldung zum Angebot. ' +
    'Ich habe die Punkte mit dem Team besprochen und wir sind mit dem Zeitplan einverstanden. ' +
    'Den Vertrag schicke ich Ihnen bis Freitag unterschrieben zurück. Für das Kick-off schlage ich ' +
    'Dienstag oder Mittwoch nächster Woche vor, jeweils ab zehn Uhr. Geben Sie mir gern kurz Bescheid, ' +
    'welcher Termin besser passt. Viele Grüße und ein schönes Wochenende, Leo';
  const WORDS = TEXT.split(' ');
  const SPEEDUP = 6;
  const lanes = [
    { el: root.querySelector('[data-lane="type"]'), wpm: 40, byChar: true },
    { el: root.querySelector('[data-lane="speak"]'), wpm: 150, byChar: false },
  ];
  const clock = root.querySelector('[data-clock]');
  const result = root.querySelector('[data-result]');
  const start = root.querySelector('[data-start]');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  const need = (wpm) => (WORDS.length / wpm) * 60; // simulierte Sekunden
  let raf = 0;

  function paint(lane, simSec) {
    const words = Math.min(WORDS.length, (simSec / 60) * lane.wpm);
    const done = words >= WORDS.length;
    let shown;
    if (lane.byChar) shown = TEXT.slice(0, Math.round((words / WORDS.length) * TEXT.length));
    else shown = WORDS.slice(0, Math.floor(words)).join(' ');
    const text = lane.el.querySelector('[data-text]');
    // Nur das Ende zeigen, damit der Cursor sichtbar bleibt
    text.textContent = shown.length > 110 ? '…' + shown.slice(-110) : shown;
    lane.el.querySelector('[data-bar]').style.width = `${(words / WORDS.length) * 100}%`;
    lane.el.querySelector('[data-count]').textContent = `${Math.floor(words)} / ${WORDS.length}`;
    lane.el.classList.toggle('is-done', done);
    return done;
  }

  function finish() {
    const tType = need(40), tSpeak = need(150);
    result.innerHTML = `Sprich: ${fmt(tSpeak)} · Tippen: ${fmt(tType)} → <em>${(tType / tSpeak).toFixed(1).replace('.', ',')}× schneller</em>`;
    start.textContent = 'Nochmal';
    start.disabled = false;
  }

  function run() {
    cancelAnimationFrame(raf);
    result.textContent = '';
    start.disabled = true;
    start.textContent = 'Läuft …';
    const total = need(40);
    if (reduced) {
      lanes.forEach((l) => paint(l, total));
      clock.textContent = fmt(total);
      return finish();
    }
    const t0 = performance.now();
    let speakAnnounced = false;
    const tick = (now) => {
      const sim = ((now - t0) / 1000) * SPEEDUP;
      clock.textContent = fmt(Math.min(sim, total));
      const speakDone = paint(lanes[1], sim);
      const typeDone = paint(lanes[0], sim);
      if (speakDone && !speakAnnounced) {
        speakAnnounced = true;
        result.innerHTML = `Sprich ist fertig nach <em>${fmt(need(150))}</em>. Tippen läuft noch …`;
      }
      if (typeDone) return finish();
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
  }

  lanes.forEach((l) => paint(l, 0));
  start.addEventListener('click', run);
})();
