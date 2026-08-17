(() => {
  const STORAGE_KEY = 'dm:theme';
  const root = document.documentElement;
  const systemTheme = () => matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';

  function updateControls() {
    const current = root.dataset.theme || systemTheme();
    const next = current === 'dark' ? 'light' : 'dark';
    document.querySelectorAll('.theme-toggle').forEach((button) => {
      button.setAttribute('aria-label', `Switch to ${next} theme`);
      button.setAttribute('title', `Switch to ${next} theme`);
    });
  }

  document.querySelectorAll('.theme-toggle').forEach((button) => {
    button.addEventListener('click', () => {
      const next = (root.dataset.theme || systemTheme()) === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem(STORAGE_KEY, next); } catch {}
      updateControls();
    });
  });

  const media = matchMedia('(prefers-color-scheme: dark)');
  media.addEventListener?.('change', () => {
    try {
      if (localStorage.getItem(STORAGE_KEY)) return;
    } catch {}
    root.dataset.theme = systemTheme();
    updateControls();
  });

  updateControls();
})();
