from django.urls import path
from .views import (
    listar_productos, detalle_producto, agregar_producto, editar_producto, eliminar_producto,
    listar_categorias, agregar_categoria, editar_categoria, eliminar_categoria,
    listar_proveedores, agregar_proveedor, editar_proveedor, eliminar_proveedor,
    inicio, listar_ventas, registrar_venta, reporte_ventas, exportar_reporte_ventas_csv,listar_clientes, agregar_cliente,editar_cliente,eliminar_cliente
)

urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio.
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/agregar/', agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),

    # Rutas para Categoría
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),

    # Rutas para Proveedor
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),

    # Rutas para Clientes
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/agregar/', agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),

    # Rutas para las ventas
    path('ventas/', listar_ventas, name='listar_ventas'),
    path('ventas/registrar/', registrar_venta, name='registrar_venta'),
    path('ventas/reporte/', reporte_ventas, name='reporte_ventas'),
    path('ventas/reporte/exportar/', exportar_reporte_ventas_csv, name='exportar_reporte_ventas_csv'),
]
