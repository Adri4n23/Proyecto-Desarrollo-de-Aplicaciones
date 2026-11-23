from django.db import models
from django.contrib.auth.models import User

# Modelo para gestionar los roles y privilegios de los usuarios
class PerfilUsuario(models.Model):
    ROLES = [
        ('Administrador', 'Administrador'),
        ('Gestor', 'Gestor'),
        ('Usuario', 'Usuario'),
        ('Visitante', 'Visitante'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='Visitante')

    def __str__(self):
        return f"{self.user.username} ({self.rol})"
