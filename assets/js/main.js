(function () {
  'use strict';

  var header = document.querySelector('.header');
  var toggle = document.querySelector('.header__toggle');
  var mobile = document.querySelector('.header__mobile');

  function onScroll() {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function setMenu(open) {
    if (!toggle || !mobile) return;
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    mobile.hidden = !open;
    header.classList.toggle('is-open', open);
  }
  if (toggle && mobile) {
    toggle.addEventListener('click', function () { setMenu(mobile.hidden); });
    mobile.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // Hero-video: pausa vid reduced motion, välj mobilkälla
  var video = document.querySelector('.hero__media video');
  if (video) {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) {
      video.removeAttribute('autoplay');
      video.pause();
    } else {
      var play = video.play();
      if (play && play.catch) play.catch(function () {});
    }
  }

  // Diskreta inträden
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  // FAQ: bara en öppen åt gången
  var faqItems = document.querySelectorAll('.faq__item');
  faqItems.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) faqItems.forEach(function (o) { if (o !== d) o.removeAttribute('open'); });
    });
  });

  // Offertformulär
  var form = document.querySelector('.form');
  if (form) {
    var status = form.querySelector('.form__status');
    var endpoint = form.getAttribute('action') || '';
    var usesPlaceholder = endpoint.indexOf('DIN-FORM-ID') !== -1 || endpoint === '';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input') && form.querySelector('.hp input').value) return;

      var data = new FormData(form);
      var btn = form.querySelector('button[type="submit"]');
      var original = btn.textContent;

      function show(ok, msg) {
        status.textContent = msg;
        status.className = 'form__status ' + (ok ? 'is-ok' : 'is-err');
      }

      if (usesPlaceholder) {
        // Reservlösning tills ett formulär-ID är satt: öppna e-postklienten med ifyllt innehåll.
        var lines = [];
        data.forEach(function (v, k) { if (k !== '_gotcha' && v) lines.push(k + ': ' + v); });
        var href = 'mailto:info@dodsboakuten.se?subject=' + encodeURIComponent('Offertförfrågan via hemsidan') +
          '&body=' + encodeURIComponent(lines.join('\n'));
        window.location.href = href;
        show(true, 'Ditt e-postprogram öppnas med förfrågan ifylld. Du kan också ringa 070-559 04 65.');
        return;
      }

      btn.disabled = true; btn.textContent = 'Skickar …';
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
        .then(function () {
          form.reset();
          show(true, 'Tack! Vi har tagit emot din förfrågan och återkommer så snart vi kan, oftast samma dag.');
        })
        .catch(function () {
          show(false, 'Något gick fel när formuläret skickades. Ring oss gärna direkt på 070-559 04 65 eller mejla info@dodsboakuten.se.');
        })
        .finally(function () { btn.disabled = false; btn.textContent = original; });
    });
  }

  // Årtal i sidfot
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
