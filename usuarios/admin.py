from django.contrib import admin
from .models import PerfilUsuario

# Registro del modelo PerfilUsuario en el panel administrativo
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'rol')
    list_filter = ('rol',)
    search_fields = ('user__username',)
