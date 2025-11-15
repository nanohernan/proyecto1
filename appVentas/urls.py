from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # URLs para Clientes
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    
    # URLs para Tiendas
    path('tiendas/', views.tienda_list, name='tienda_list'),
    path('tiendas/crear/', views.tienda_create, name='tienda_create'),
    path('tiendas/editar/<int:pk>/', views.tienda_update, name='tienda_update'),
    path('tiendas/eliminar/<int:pk>/', views.tienda_delete, name='tienda_delete'),
    
    # URLs para Compras
    path('compras/', views.compra_list, name='compra_list'),
    path('compras/crear/', views.compra_create, name='compra_create'),
    path('compras/editar/<int:pk>/', views.compra_update, name='compra_update'),
    path('compras/eliminar/<int:pk>/', views.compra_delete, name='compra_delete'),
]
