document.addEventListener("DOMContentLoaded", function() {
    const toggleBtn = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');

    if(toggleBtn && sidebar){
        toggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('-translate-x-full');
        });
    }

    // Toggle submenus
    document.querySelectorAll('.agenda-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
            const submenu = btn.nextElementSibling;
            submenu.classList.toggle('hidden');
            const icon = btn.querySelector('svg');
            icon.classList.toggle('rotate-180');
        });
    });
});
