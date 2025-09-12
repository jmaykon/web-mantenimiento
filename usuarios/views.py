from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_usuario(request):
    return render(request, "usuarios/dashboard_usuario.html")


def solicitar_mantenimiento(request):
    return render(request, "usuarios/solicitar_mantenimiento.html")


def mis_solicitudes(request):
    # Aquí luego mostrarás las solicitudes del usuario logueado
    return render(request, "usuarios/mis_solicitudes.html")

def cambiar_password(request):
    usuario_id = request.session.get("usuario_id")
    if not usuario_id:
        return redirect("login:login")

    usuario = get_object_or_404(Usuarios, id=usuario_id)

    if request.method == "POST":
        new_password1 = request.POST.get("new_password1")
        new_password2 = request.POST.get("new_password2")

        if new_password1 != new_password2:
            messages.error(request, "❌ Las nuevas contraseñas no coinciden.")
            return redirect("usuarios:perfil_usuario")

        usuario.password_hash = make_password(new_password1)
        usuario.save()
        messages.success(request, "✅ Contraseña actualizada correctamente.")
        return redirect("usuarios:perfil_usuario")

    return redirect("usuarios:perfil_usuario")


#MANTENIMIENTO
def solicitar_mantenimiento(request):
    return render(request, "usuarios/solicitar_mantenimiento.html")


#SOLICITUDES
def lista_mantenimiento(request):
    return render(request, "usuarios/lista_mantenimiento.html")

    usuarios = Usuario.objects.all().values('id', 'solicitud_id', 'fecha_programada', 'tecnico_asignado', 'observaciones', 'estado')
    usuarios_list = list(usuarios)
    return JsonResponse({'usuarios': usuarios_list})

#AGENDA
def agenda_mantenimiento(request):
    return render(request, "usuarios/agenda_mantenimiento.html")


def perfil_usuario_view(request):
    usuario_id = request.session.get("usuario_id")
    if not usuario_id:
        return redirect('login:login')
    
    usuario = get_object_or_404(Usuarios, id=usuario_id)
    return render(request, "usuarios/perfil_usuario.html", {"usuario": usuario})











