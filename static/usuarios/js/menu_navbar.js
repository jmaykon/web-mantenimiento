document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("menu-toggle");
    const sidebar = document.getElementById("sidebar");

    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener("click", () => {
            sidebar.classList.toggle("-translate-x-full");
        });
    }

    // Extra: submenús de agenda
    document.querySelectorAll(".agenda-toggle").forEach(button => {
        button.addEventListener("click", () => {
            const submenu = button.nextElementSibling;
            submenu.classList.toggle("hidden");
            button.querySelector("svg").classList.toggle("rotate-180");
        });
    });
});
