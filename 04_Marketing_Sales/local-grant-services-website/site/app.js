const menuButton = document.querySelector(".menu-toggle");
const siteNav = document.querySelector("#site-nav");
const form = document.querySelector(".contact-form");
const formNote = document.querySelector(".form-note");

if (menuButton && siteNav) {
  menuButton.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(isOpen));
  });

  siteNav.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      siteNav.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
    }
  });
}

if (form && formNote) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    formNote.textContent = "Inquiry captured for demo. Connect this form to a CRM before launch.";
    form.reset();
  });
}

