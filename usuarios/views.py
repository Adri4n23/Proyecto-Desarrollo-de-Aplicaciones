from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import PerfilUsuario

# Vista para registrar nuevos usuarios con rol Visitante por defecto
def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            PerfilUsuario.objects.create(user=user, rol='Visitante')
            login(request, user)
            return redirect('panel_roles')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Vista para iniciar sesion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('panel_roles')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

# Vista para cerrar sesion
def logout_view(request):
    logout(request)
    return redirect('login')

# Vista principal que muestra contenido segun el rol del usuario
@login_required
def panel_roles_view(request):
    perfil, _ = PerfilUsuario.objects.get_or_create(user=request.user)
    return render(request, 'usuarios/panel.html', {'rol': perfil.rol})
