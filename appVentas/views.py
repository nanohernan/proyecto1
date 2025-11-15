from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Cliente, Tienda, Compra
from .forms import ClienteForm, TiendaForm, CompraForm

# Función para verificar si es usuario con permisos CRUD
def es_usuario_crud(user):
    return user.username == 'admin'

# Función para verificar si es usuario con permisos RU
def es_usuario_ru(user):
    return user.username == 'tecnico01'

# Página inicial
def home(request):
    return render(request, 'home.html')

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# CRUD para Clientes
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/list.html', {'clientes': clientes})

@login_required
def cliente_create(request):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para crear clientes")
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Crear Cliente'})

@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Editar Cliente'})

@login_required
def cliente_delete(request, pk):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para eliminar clientes")
    
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/delete.html', {'cliente': cliente})

# CRUD para Tiendas
@login_required
def tienda_list(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas/list.html', {'tiendas': tiendas})

@login_required
def tienda_create(request):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para crear tiendas")
    
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tienda_list')
    else:
        form = TiendaForm()
    return render(request, 'tiendas/form.html', {'form': form, 'titulo': 'Crear Tienda'})

@login_required
def tienda_update(request, pk):
    tienda = get_object_or_404(Tienda, pk=pk)
    if request.method == 'POST':
        form = TiendaForm(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
            return redirect('tienda_list')
    else:
        form = TiendaForm(instance=tienda)
    return render(request, 'tiendas/form.html', {'form': form, 'titulo': 'Editar Tienda'})

@login_required
def tienda_delete(request, pk):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para eliminar tiendas")
    
    tienda = get_object_or_404(Tienda, pk=pk)
    if request.method == 'POST':
        tienda.delete()
        return redirect('tienda_list')
    return render(request, 'tiendas/delete.html', {'tienda': tienda})

# CRUD para Compras
@login_required
def compra_list(request):
    compras = Compra.objects.all()
    return render(request, 'compras/list.html', {'compras': compras})

@login_required
def compra_create(request):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para crear compras")
    
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm()
    return render(request, 'compras/form.html', {'form': form, 'titulo': 'Crear Compra'})

@login_required
def compra_update(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect('compra_list')
    else:
        form = CompraForm(instance=compra)
    return render(request, 'compras/form.html', {'form': form, 'titulo': 'Editar Compra'})

@login_required
def compra_delete(request, pk):
    if not es_usuario_crud(request.user):
        return HttpResponseForbidden("No tienes permisos para eliminar compras")
    
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('compra_list')
    return render(request, 'compras/delete.html', {'compra': compra})
