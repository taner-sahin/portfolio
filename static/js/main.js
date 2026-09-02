document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

  function setActiveLink() {
    const currentHash = window.location.hash;

    navLinks.forEach((link) => {
      link.classList.remove("active");

      const href = link.getAttribute("href");

      if (!currentHash && href === "/") {
        link.classList.add("active");
      }

      if (currentHash && href === currentHash) {
        link.classList.add("active");
      }
    });
  }

  setActiveLink();

  window.addEventListener("hashchange", setActiveLink);
});