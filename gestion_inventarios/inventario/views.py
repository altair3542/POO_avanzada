import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_date
from django.http import HttpResponse
from .models import Producto, Categoria, Proveedor, DetalleProducto, Ventas, Cliente
from .forms import ProductoForm, CategoriaForm, ProveedorForm, DetalleProductoForm, ClienteForm, VentasForm

# Create your views here.

def inicio(request):
    return render(request, 'inventario/inicio.html')

def listar_productos(request):
    # Obtiene todos los productos de la base de datos, incluyendo sus detalles relacionados,
    # utilizando `prefetch_related` para optimizar la consulta y evitar múltiples consultas adicionales.
    productos = Producto.objects.prefetch_related('detalleproducto').all()

    # Renderiza la plantilla 'inventario/listar_productos.html' y pasa la lista de productos al contexto
    # para que puedan ser utilizados dentro del template.
    return render(request, 'inventario/listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        detalle_form = DetalleProductoForm(request.POST)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.save()
            producto_form.save_m2m()

            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save

            return redirect('listar_productos')

    else:
        producto_form = ProductoForm()
        detalle_form = DetalleProductoForm()

    return render(request, 'inventario/agregar_producto.html', {
         'producto_form': producto_form,
         'detalle_form': detalle_form
     })

from django.shortcuts import get_object_or_404

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/detalle_producto.html', {'producto': producto})


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    try:
        detalle = producto.detalleproducto
    except DetalleProducto.DoesNotExist:
        detalle = None

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        detalle_form = DetalleProductoForm(request.POST, instance=detalle)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save(commit=False)
            producto_form.save()
            producto_form.save_m2m() # guardar relaciones muchos a muchos.
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('listar_productos')
    else:
        producto_form = ProductoForm(instance=producto)
        detalle_form = DetalleProductoForm(instance=detalle)
    return render(request, 'inventario/editar_producto.html', {
        'producto_form': producto_form,
        'detalle_form': detalle_form
    })

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'inventario/eliminar_producto.html', {'producto': producto})

# Vistas para Categoria
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'inventario/listar_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'inventario/agregar_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'inventario/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'inventario/eliminar_categoria.html', {'categoria': categoria})

# Vistas para Proveedor
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'inventario/listar_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'inventario/agregar_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'inventario/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'inventario/eliminar_proveedor.html', {'proveedor': proveedor})

#vistas para ventas e informes
def listar_ventas(request):
    ventas = Ventas.objects.all().select_related('producto', 'cliente')
    return render(request, 'inventario/listar_ventas.html', {'ventas': ventas})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = venta.producto

            # Verificar si hay suficiente stock (cantidad) antes de registrar la venta
            if producto.cantidad >= venta.cantidad:
                # Calcular el total de la venta
                venta.total = producto.precio * venta.cantidad

                # Reducir la cantidad (stock) del producto
                producto.cantidad -= venta.cantidad
                producto.save()

                venta.save()  # Guardar la venta con el total calculado
                return redirect('listar_ventas')
            else:
                form.add_error('cantidad', 'No hay suficiente stock para realizar esta venta.')
    else:
        form = VentasForm()

    return render(request, 'inventario/registrar_venta.html', {'form': form})

def reporte_ventas(request):
    ventas = Ventas.objects.all()
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    cliente_id = request.GET.get('cliente_id')
    producto_id = request.GET.get('producto_id')

    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha_venta__range=[parse_date(fecha_inicio), parse_date(fecha_fin)])

    if cliente_id:
        ventas = ventas.filter(cliente_id=cliente_id)

    if producto_id:
        ventas = ventas.filter(producto_id=producto_id)

    return render(request, 'inventario/reporte_ventas.html', {'ventas': ventas})

def exportar_reporte_ventas_csv(request):
    ventas = Ventas.objects.all()

    # Filtros por fecha, cliente y producto
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    cliente_id = request.GET.get('cliente_id')
    producto_id = request.GET.get('producto_id')

    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha_venta__range=[parse_date(fecha_inicio), parse_date(fecha_fin)])

    if cliente_id:
        ventas = ventas.filter(cliente_id=cliente_id)

    if producto_id:
        ventas = ventas.filter(producto_id=producto_id)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_ventas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha de Venta', 'Producto', 'Cliente', 'Cantidad', 'Total'])

    for venta in ventas:
        writer.writerow([venta.fecha_venta, venta.producto.nombre, venta.cliente.nombre, venta.cantidad, venta.total])

    return response

#vistas para cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'inventario/listar_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'inventario/agregar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'inventario/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'inventario/eliminar_cliente.html', {'cliente': cliente})
