from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_view, name='login'),         # Formulario de login
    path('logout/', views.logout_view, name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),  # Redirige según rol
]
