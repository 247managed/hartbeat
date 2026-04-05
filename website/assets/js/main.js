/* Hart Beat Energy — Main JS */
(function() {
  'use strict';

  // Mobile nav toggle
  const toggle = document.querySelector('.nav__toggle');
  const mobileNav = document.querySelector('.nav__mobile');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', () => {
      mobileNav.classList.toggle('is-open');
      const expanded = mobileNav.classList.contains('is-open');
      toggle.setAttribute('aria-expanded', expanded);
      document.body.style.overflow = expanded ? 'hidden' : '';
    });
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      mobileNav.classList.remove('is-open');
      document.body.style.overflow = '';
    }));
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href');
      if (id.length > 1) {
        const el = document.querySelector(id);
        if (el) { e.preventDefault(); el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
      }
    });
  });

  // Savings calculator
  const calc = document.querySelector('[data-calc]');
  if (calc) {
    const bill = calc.querySelector('[data-calc-bill]');
    const years = calc.querySelector('[data-calc-years]');
    const out20 = calc.querySelector('[data-calc-out-20]');
    const outLease = calc.querySelector('[data-calc-out-lease]');
    const outBill = calc.querySelector('[data-calc-out-bill]');
    function run() {
      const monthly = Number(bill.value) || 0;
      const y = Number(years.value) || 20;
      // Assume 20% avg bill reduction via lease/PPA, 3% annual utility rate escalator
      const leaseSavings = monthly * 0.20 * 12 * y;
      // 20-year cumulative utility cost at 3% escalator vs flat
      let cumulative = 0;
      for (let i = 0; i < y; i++) { cumulative += monthly * 12 * Math.pow(1.03, i); }
      if (out20) out20.textContent = '$' + Math.round(cumulative).toLocaleString();
      if (outLease) outLease.textContent = '$' + Math.round(leaseSavings).toLocaleString();
      if (outBill) outBill.textContent = '$' + (monthly * 0.80).toFixed(0);
    }
    if (bill) bill.addEventListener('input', run);
    if (years) years.addEventListener('input', run);
    run();
  }

  // Form submission (intercepts and shows success — replace with real endpoint)
  document.querySelectorAll('form[data-form]').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const success = form.querySelector('[data-form-success]');
      const submit = form.querySelector('[type="submit"]');
      if (submit) { submit.disabled = true; submit.textContent = 'Sending…'; }
      // TODO: wire to real backend (Formspree, Netlify Forms, or custom endpoint)
      setTimeout(() => {
        form.style.display = 'none';
        if (success) success.style.display = 'block';
      }, 600);
    });
  });

  // FAQ — close others when one opens (single-open accordion, optional)
  document.querySelectorAll('.faq[data-single] details').forEach(d => {
    d.addEventListener('toggle', () => {
      if (d.open) {
        d.parentElement.querySelectorAll('details').forEach(o => { if (o !== d) o.open = false; });
      }
    });
  });

  // Sticky nav shadow on scroll
  const nav = document.querySelector('.nav');
  if (nav) {
    let last = 0;
    window.addEventListener('scroll', () => {
      const y = window.scrollY;
      nav.style.boxShadow = y > 4 ? '0 2px 14px rgba(11,31,58,.08)' : 'none';
      last = y;
    }, { passive: true });
  }
})();
