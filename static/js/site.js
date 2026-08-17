(() => {
  const platform = String(navigator.userAgentData?.platform || navigator.platform || navigator.userAgent).toLowerCase();
  const detectedOS = platform.includes('win')
    ? 'windows'
    : platform.includes('linux')
      ? 'linux'
      : platform.includes('mac')
        ? 'macos'
        : null;

  document.querySelectorAll('[data-tabs]').forEach((group) => {
    const tabs = [...group.querySelectorAll('[role="tab"][data-tab]')];
    const syncHash = group.hasAttribute('data-sync-hash');

    function selectTab(selected, focus = false) {
      tabs.forEach((tab) => {
        const active = tab === selected;
        const panel = document.getElementById(tab.getAttribute('aria-controls'));
        tab.classList.toggle('active', active);
        tab.setAttribute('aria-selected', String(active));
        tab.tabIndex = active ? 0 : -1;
        if (panel) {
          panel.classList.toggle('active', active);
          panel.hidden = !active;
        }
      });
      if (focus) selected.focus();
    }

    function tabForHash() {
      return tabs.find((tab) => `#${tab.getAttribute('aria-controls')}` === location.hash);
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => {
        selectTab(tab);
        if (syncHash) history.replaceState(null, '', `#${tab.getAttribute('aria-controls')}`);
      });
      tab.addEventListener('keydown', (event) => {
        if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
        event.preventDefault();
        const nextIndex = event.key === 'Home'
          ? 0
          : event.key === 'End'
            ? tabs.length - 1
            : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
        selectTab(tabs[nextIndex], true);
      });
    });

    const linkedTab = syncHash ? tabForHash() : null;
    if (linkedTab) {
      selectTab(linkedTab);
      requestAnimationFrame(() => {
        document.getElementById(linkedTab.getAttribute('aria-controls'))?.scrollIntoView();
      });
    } else if (group.hasAttribute('data-detect-os') && detectedOS) {
      const detectedTab = tabs.find((tab) => tab.dataset.tab === detectedOS);
      if (detectedTab) selectTab(detectedTab);
    }

    if (syncHash) {
      window.addEventListener('hashchange', () => {
        const selected = tabForHash();
        if (!selected) return;
        selectTab(selected);
        document.getElementById(selected.getAttribute('aria-controls'))?.scrollIntoView();
      });
    }
  });

  const COPY_ICON = '<svg viewBox="0 0 16 16" aria-hidden="true"><use href="/icons/bootstrap-icons.svg#bi-clipboard"/></svg>';
  const CHECK_ICON = '<svg viewBox="0 0 16 16" aria-hidden="true"><use href="/icons/bootstrap-icons.svg#bi-check-lg"/></svg>';

  document.querySelectorAll('.copy-btn').forEach((button) => {
    button.addEventListener('click', async () => {
      const terminal = button.closest('.install-terminal');
      const command = terminal?.querySelector('.t-cmd')?.textContent;
      const status = terminal?.querySelector('.copy-status');
      const defaultLabel = button.dataset.copyLabel || 'Copy command';
      if (!command) return;
      try {
        await navigator.clipboard.writeText(command);
        button.innerHTML = CHECK_ICON;
        button.classList.add('copied');
        button.setAttribute('aria-label', 'Copied');
        if (status) status.textContent = 'Command copied.';
        setTimeout(() => {
          button.innerHTML = COPY_ICON;
          button.classList.remove('copied');
          button.setAttribute('aria-label', defaultLabel);
        }, 1500);
      } catch {
        button.setAttribute('aria-label', 'Copy failed');
        if (status) status.textContent = 'Copy failed. Select and copy the command manually.';
      }
    });
  });

  const lightbox = document.querySelector('[data-lightbox]');
  const lightboxClose = lightbox?.querySelector('[data-lightbox-close]');
  const lightboxImage = lightbox?.querySelector('[data-lightbox-image]');
  const lightboxTitle = lightbox?.querySelector('[data-lightbox-title]');
  const defaultLightboxMedia = lightboxImage && lightboxTitle
    ? {
        src: lightboxImage.getAttribute('src'),
        alt: lightboxImage.getAttribute('alt'),
        width: lightboxImage.getAttribute('width'),
        height: lightboxImage.getAttribute('height'),
        title: lightboxTitle.textContent,
      }
    : null;
  let lightboxOpener = null;

  function setLightbox(open, opener = null) {
    if (!lightbox) return;
    if (open) {
      const media = opener?.dataset.lightboxSrc
        ? {
            src: opener.dataset.lightboxSrc,
            alt: opener.dataset.lightboxAlt || '',
            width: opener.dataset.lightboxWidth || '',
            height: opener.dataset.lightboxHeight || '',
            title: opener.dataset.lightboxTitle || 'omnideck',
          }
        : defaultLightboxMedia;
      if (media && lightboxImage && lightboxTitle) {
        lightboxImage.setAttribute('src', media.src);
        lightboxImage.setAttribute('alt', media.alt);
        if (media.width) lightboxImage.setAttribute('width', media.width);
        if (media.height) lightboxImage.setAttribute('height', media.height);
        lightboxTitle.textContent = media.title;
      }
      lightboxOpener = opener;
      lightbox.showModal();
      document.body.classList.add('lightbox-open');
      lightboxClose?.focus();
    } else {
      lightbox.close();
    }
  }

  document.querySelectorAll('[data-lightbox-open]').forEach((button) => {
    button.addEventListener('click', () => setLightbox(true, button));
  });
  lightboxClose?.addEventListener('click', () => setLightbox(false));
  lightbox?.addEventListener('click', (event) => {
    if (event.target === lightbox) setLightbox(false);
  });
  lightbox?.addEventListener('close', () => {
    document.body.classList.remove('lightbox-open');
    lightboxOpener?.focus();
    lightboxOpener = null;
  });

  const navToggle = document.querySelector('.nav-toggle');
  const navMobile = document.querySelector('.nav-mobile');
  const navBackdrop = document.querySelector('.nav-backdrop');

  function setMenu(open) {
    if (!navToggle || !navMobile) return;
    navMobile.classList.toggle('open', open);
    navToggle.classList.toggle('active', open);
    navBackdrop?.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navMobile.setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('menu-open', open);
    if (open) navMobile.querySelector('a')?.focus();
  }

  navToggle?.addEventListener('click', () => setMenu(!navMobile?.classList.contains('open')));
  navBackdrop?.addEventListener('click', () => setMenu(false));
  navMobile?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && navMobile?.classList.contains('open')) {
      setMenu(false);
      navToggle?.focus();
    }
  });

  const path = location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('.nav-link, .nav-mobile-link').forEach((link) => {
    const href = new URL(link.href, location.origin).pathname.replace(/index\.html$/, '');
    const isSection = href !== '/' && href.endsWith('/') && path.startsWith(href);
    if (href === path || isSection) link.setAttribute('aria-current', 'page');
  });

  const docsLinks = [...document.querySelectorAll('.docs-sidebar a, .docs-mobile-nav a')];
  function updateDocsCurrent() {
    const matchingAnchor = docsLinks.find((link) => {
      const url = new URL(link.href, location.origin);
      return url.pathname.replace(/index\.html$/, '') === path && url.hash === location.hash && url.hash;
    });
    docsLinks.forEach((link) => {
      const url = new URL(link.href, location.origin);
      const linkPath = url.pathname.replace(/index\.html$/, '');
      const current = matchingAnchor ? link === matchingAnchor : linkPath === path && !url.hash;
      if (current) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
  }
  updateDocsCurrent();
  window.addEventListener('hashchange', updateDocsCurrent);
})();
