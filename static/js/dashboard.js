import { sidebarAdminHTML } from '/static/js/sidebar_admin.js';
import { sidebarUsuarioHTML } from '/static/js/sidebar_usuario.js';
import { sidebarTecnicoHTML } from '/static/js/sidebar_tecnico.js';

document.addEventListener('DOMContentLoaded', () => {
    const sidebarContainer = document.getElementById('sidebar');
    const usernameDisplay = document.getElementById('username-display');
    const rolDisplay = document.getElementById('rol-display');

    // Tomamos usuario y rol de sessionStorage (seteado en el login)
    const username = sessionStorage.getItem('username');
    const rol = sessionStorage.getItem('rol');

    if(username && rol){
        usernameDisplay.textContent = `Hola, ${username}`;
        rolDisplay.textContent = rol;

        switch(rol.toLowerCase()){
            case 'admin':
                sidebarContainer.innerHTML = sidebarAdminHTML;
                break;
            case 'usuario':
                sidebarContainer.innerHTML = sidebarUsuarioHTML;
                break;
            case 'tecnico':
                sidebarContainer.innerHTML = sidebarTecnicoHTML;
                break;
        }
    }
});
if(!username && document.cookie){
    const cookieUsername = document.cookie.split('; ').find(row => row.startsWith('username='));
    const cookieRol = document.cookie.split('; ').find(row => row.startsWith('rol='));
    if(cookieUsername && cookieRol){
        sessionStorage.setItem('username', cookieUsername.split('=')[1]);
        sessionStorage.setItem('rol', cookieRol.split('=')[1]);
        location.reload(); // recarga la página con datos
    }
}
