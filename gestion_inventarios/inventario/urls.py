from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from .views import (
#     listar_productos, detalle_producto, agregar_producto, editar_producto, eliminar_producto,
#     listar_categorias, agregar_categoria, editar_categoria, eliminar_categoria,
#     listar_proveedores, agregar_proveedor, editar_proveedor, eliminar_proveedor,
#     inicio, listar_ventas, registrar_venta, reporte_ventas, exportar_reporte_ventas_csv,listar_clientes, agregar_cliente,editar_cliente,eliminar_cliente, exportar_reporte_ventas_excel, exportar_reporte_ventas_pdf
# )

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('', views.inicio, name='inicio'),  # Ruta para la página de inicio.
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),

    # Rutas para Categoría
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),

    # Rutas para Proveedor
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),

    # Rutas para Clientes
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    # Rutas para las ventas
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
    path('ventas/reporte/', views.reporte_ventas, name='reporte_ventas'),
    path('ventas/reporte/exportar/', views.exportar_reporte_ventas_csv, name='exportar_reporte_ventas_csv'),
    path('ventas/reporte/exportar-excel/', views.exportar_reporte_ventas_excel, name='exportar_reporte_ventas_excel'),
    path('ventas/reporte/exportar-pdf/', views.exportar_reporte_ventas_pdf, name='exportar_reporte_ventas_pdf'),
]
