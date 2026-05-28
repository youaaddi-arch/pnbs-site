/* Formapro — interactions légères (menu mobile + formulaire de contact) */
(function () {
  "use strict";

  // Menu mobile
  var toggle = document.querySelector(".nav__toggle");
  var links = document.querySelector(".nav__links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { links.classList.remove("is-open"); });
    });
  }

  // Marque le lien de navigation actif selon la page courante
  var path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav__links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) {
      a.classList.add("is-active");
    }
  });

  // Formulaire de contact (démo : pas de backend, simulation d'envoi)
  var form = document.querySelector("#contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var msg = document.querySelector("#form-msg");
      var btn = form.querySelector("button[type=submit]");
      if (btn) { btn.disabled = true; btn.textContent = "Envoi…"; }
      // Simulation. Pour un envoi réel, branchez Formspree / un endpoint /api.
      setTimeout(function () {
        if (msg) {
          msg.classList.add("is-visible");
          msg.textContent = "Merci ! Votre demande a bien été enregistrée. Nous vous répondons sous 24 h.";
        }
        form.reset();
        if (btn) { btn.disabled = false; btn.textContent = "Envoyer ma demande"; }
      }, 700);
    });
  }

  // Année dynamique dans le footer
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
