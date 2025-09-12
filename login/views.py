from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse



def login_view(request):
    error = None

    # Si hay un usuario autenticado en la sesión, cerrarla
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')

        user = authenticate(request, username=username, password=password)
        if user:
            # Loguea al usuario
            login(request, user)

            # Redirige según rol usando la sesión del usuario
            rol = user.rol.lower()
            if rol == 'admin':
                redirect_url = reverse('adminapp:dashboard_admin')
            elif rol == 'usuario':
                redirect_url = reverse('usuarios:dashboard_usuario')
            else:
                redirect_url = reverse('tecnicos:dashboard_tecnico')

            response = redirect(redirect_url)

            # Cookies solo para precargar username (opcional)
            if remember_me:
                response.set_cookie('username', user.username, max_age=7*24*60*60)
            else:
                response.delete_cookie('username')

            return response
        else:
            error = "Usuario o contraseña incorrectos"

    username_cookie = request.COOKIES.get('username')
    return render(request, 'login/login.html', {'error': error, 'username_cookie': username_cookie})



def logout_view(request):
    logout(request)
    response = redirect('login:login')
    response.delete_cookie('username')
    return response

@login_required
def dashboard(request):
    rol = request.user.rol.lower()
    if rol == 'admin':
        template = 'adminapp/dashboard_admin.html'
    elif rol == 'usuario':
        template = 'usuarios/dashboard_usuario.html'
    elif rol == 'tecnico':
        template = 'tecnicos/dashboard_tecnico.html'
    else:
        return redirect('login:login')
    return render(request, template)
