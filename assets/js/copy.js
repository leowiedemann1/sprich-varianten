// V5: Promo-Code mit einem Klick kopieren.
document.querySelectorAll('[data-copy]').forEach((btn) => {
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
      btn.textContent = 'Kopiert ✓';
      btn.classList.add('is-copied');
      setTimeout(() => { btn.textContent = 'Kopieren'; btn.classList.remove('is-copied'); }, 1800);
    } catch {
      btn.textContent = btn.dataset.copy;
    }
  });
});
