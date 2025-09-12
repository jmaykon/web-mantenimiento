# login/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ADMIN = "admin"
    USUARIO = "usuario"
    TECNICO = "tecnico"

    ROLE_CHOICES = [
        (ADMIN, "Administrador"),
        (USUARIO, "Usuario"),
        (TECNICO, "Técnico"),
    ]

    rol = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USUARIO)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
