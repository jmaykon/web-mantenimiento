from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),          # tu app login
    path('usuarios/', include('usuarios.urls')),    # app usuarios
    path('adminapp/', include('adminapp.urls')),    # app adminapp
    path('dashboard/', include('dashboard.urls')),  # app técnicos
    
    path('', lambda request: redirect('login:login')),  # raíz redirige al login
]
