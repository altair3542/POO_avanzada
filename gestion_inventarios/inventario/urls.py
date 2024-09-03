from django.urls import path
from .views import (
    listar_productos, agregar_producto, editar_producto, eliminar_producto,
    listar_categorias, agregar_categoria, editar_categoria, eliminar_categoria,
    listar_proveedores, agregar_proveedor, editar_proveedor, eliminar_proveedor,
    inicio
)


urlpatterns = [
    path('', inicio, name='inicio'),  # Ruta para la página de inicio.
    path('productos/', listar_productos, name='listar_productos'),  # Ruta para listar productos.
    path('productos/agregar/', agregar_producto, name='agregar_producto'),  # Ruta para agregar un nuevo producto.
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),  # Ruta para editar un producto existente.
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),  # Ruta para eliminar un producto.


# Rutas para Categoria
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),

    # Rutas para Proveedor
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),
]
