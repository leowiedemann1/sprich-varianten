// V3: drei Runden füllen sich nacheinander bis 10.000 Wörter, sobald die Card sichtbar ist.
(() => {
  const root = document.querySelector('[data-challenge]');
  if (!root) return;
  const rounds = [...root.querySelectorAll('[data-round]')];
  const total = root.querySelector('[data-total]');
  const GOAL = 10000, DURATION = 1400, GAP = 250;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const nf = new Intl.NumberFormat('de-DE');

  const set = (round, words) => {
    round.querySelector('[data-bar]').style.width = `${(words / GOAL) * 100}%`;
    round.querySelector('[data-count]').textContent = nf.format(Math.round(words));
  };
  const markDone = (i) => {
    rounds[i].classList.add('is-done');
    total.textContent = `${i + 1} von 3 Monaten zurück`;
  };

  function animate(i) {
    if (i >= rounds.length) return;
    const t0 = performance.now();
    const step = (now) => {
      const p = Math.min(1, (now - t0) / DURATION);
      set(rounds[i], GOAL * (1 - Math.pow(1 - p, 3)));
      if (p < 1) return requestAnimationFrame(step);
      markDone(i);
      setTimeout(() => animate(i + 1), GAP);
    };
    requestAnimationFrame(step);
  }

  function play() {
    if (reduced) return rounds.forEach((r, i) => { set(r, GOAL); markDone(i); });
    animate(0);
  }

  const io = new IntersectionObserver((entries) => {
    if (entries.some((e) => e.isIntersecting)) { io.disconnect(); play(); }
  }, { threshold: 0.4 });
  io.observe(root);
})();
