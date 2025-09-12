
# usuarios/urls.py
from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('dashboard/', views.dashboard_usuario, name="dashboard_usuario"),
    path("perfil/", views.perfil_usuario_view, name="perfil_usuario"),  # 👈 usa tu vista correcta
    path("cambiar-password/", views.cambiar_password, name="cambiar_password"),
    path("solicitar-mantenimiento/", views.solicitar_mantenimiento, name="solicitar_mantenimiento"),
    path("lista-mantenimiento/", views.lista_mantenimiento, name="lista_mantenimiento"),
    path("agenda-mantenimiento/", views.agenda_mantenimiento, name="agenda_mantenimiento"),
   
]
