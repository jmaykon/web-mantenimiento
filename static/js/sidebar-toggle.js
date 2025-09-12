document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("menu-toggle");
    const sidebar = document.getElementById("sidebar");
    if (btn && sidebar) {
        btn.addEventListener("click", () => {
            sidebar.classList.toggle("-translate-x-full");
        });
    }
});
