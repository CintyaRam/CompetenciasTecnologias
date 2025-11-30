from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Etiqueta, Detalle
from .forms import ProductoForm, CategoriaForm, EtiquetaForm, DetalleForm
from django.db.models import Count, Avg, Max, Min
from django.db import connection


def index(request):
    return render(request, "index.html")


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


def crear_producto(request):
    if request.method == "POST":
        form_producto = ProductoForm(request.POST)
        form_detalle = DetalleForm(request.POST)

        if form_producto.is_valid() and form_detalle.is_valid():
            detalle = form_detalle.save()
            producto = form_producto.save(commit=False)
            producto.detalle = detalle
            producto.save()
            form_producto.save_m2m()

            return redirect("lista_productos")
    else:
        form_producto = ProductoForm()
        form_detalle = DetalleForm()

    return render(request, "productos/crear.html", {
        "form_producto": form_producto,
        "form_detalle": form_detalle
    })


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "productos/detalle.html", {"producto": producto})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    detalle = producto.detalle

    if request.method == "POST":
        form_producto = ProductoForm(request.POST, instance=producto)
        form_detalle = DetalleForm(request.POST, instance=detalle)

        if form_producto.is_valid() and form_detalle.is_valid():
            form_detalle.save()
            form_producto.save()
            return redirect("lista_productos")

    else:
        form_producto = ProductoForm(instance=producto)
        form_detalle = DetalleForm(instance=detalle)

    return render(request, "productos/editar.html", {
        "form_producto": form_producto,
        "form_detalle": form_detalle
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.delete()
        return redirect("lista_productos")

    return render(request, "productos/eliminar.html", {"producto": producto})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias/lista.html", {"categorias": categorias})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_categorias")
    else:
        form = CategoriaForm()

    return render(request, "categorias/formulario.html", {"form": form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("lista_categorias")
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, "categorias/formulario.html", {"form": form})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        categoria.delete()
        return redirect("lista_categorias")

    return render(request, "categorias/eliminar.html", {"categoria": categoria})


def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, "etiquetas/lista.html", {"etiquetas": etiquetas})


def crear_etiqueta(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm()

    return render(request, "etiquetas/formulario.html", {"form": form})


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm(instance=etiqueta)

    return render(request, "etiquetas/formulario.html", {"form": form})


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == "POST":
        etiqueta.delete()
        return redirect("lista_etiquetas")

    return render(request, "etiquetas/eliminar.html", {"etiqueta": etiqueta})


def consultas_orm(request):
    # 1. Productos con precio mayor a 10.000
    productos_mayor_10000 = Producto.objects.filter(precio__gt=10000)

    # 2. Productos ordenados por precio desc
    productos_ordenados_desc = Producto.objects.order_by('-precio')

    # 3. Categorías con cantidad de productos (annotate)
    categorias_con_cantidad = Categoria.objects.annotate(
        total_productos=Count('productos')
    )

    # 4. Productos que pertenecen a una categoría específica (ej: id = 1)
    productos_categoria_1 = Producto.objects.filter(categoria_id=1)

    # 5. Productos que tienen una etiqueta específica (ej: id = 1)
    productos_etiqueta_1 = Producto.objects.filter(etiquetas__id=1)

    # 6. Precio promedio de todos los productos
    precio_promedio = Producto.objects.all().aggregate(Avg('precio'))

    # 7. Producto más caro
    producto_mas_caro = Producto.objects.all().aggregate(Max('precio'))

    # 8. Producto más barato
    producto_mas_barato = Producto.objects.all().aggregate(Min('precio'))

    # 9. Productos que NO tienen etiquetas
    productos_sin_etiquetas = Producto.objects.filter(etiquetas__isnull=True)

    # 10. Etiquetas más usadas (ordenadas por cantidad)
    etiquetas_ordenadas = Etiqueta.objects.annotate(
        total_usos=Count('productos')
    ).order_by('-total_usos')


    # 11. Productos que NO pertenecen a la categoría con ID = 1
    productos_excluye_categoria_1 = Producto.objects.exclude(categoria_id=1)

    contexto = {
    'productos_mayor_10000': productos_mayor_10000,
    'productos_ordenados_desc': productos_ordenados_desc,
    'categorias_con_cantidad': categorias_con_cantidad,
    'productos_categoria_1': productos_categoria_1,
    'productos_etiqueta_1': productos_etiqueta_1,
    'precio_promedio': precio_promedio,
    'producto_mas_caro': producto_mas_caro,
    'producto_mas_barato': producto_mas_barato,
    'productos_sin_etiquetas': productos_sin_etiquetas,
    'etiquetas_ordenadas': etiquetas_ordenadas,
    'productos_excluye_categoria_1': productos_excluye_categoria_1,
    }

    return render(request, "consultas/orm.html", contexto)


def consultas_raw(request):

    # RAW 1: Productos con precio mayor a 10.000
    productos_mayor_10000 = Producto.objects.raw(
        "SELECT * FROM gestion_producto WHERE precio > 10000"
    )

    # RAW 2: Ordenar productos por precio DESC
    productos_ordenados_desc = Producto.objects.raw(
        "SELECT * FROM gestion_producto ORDER BY precio DESC"
    )

    # RAW 3: Join manual entre productos y categorías
    productos_con_categoria = Producto.objects.raw("""
        SELECT p.id, p.nombre, p.precio, c.nombre AS categoria_nombre
        FROM gestion_producto p
        INNER JOIN gestion_categoria c ON p.categoria_id = c.id
    """)

    # RAW 4: Raw con parámetro (ejemplo: categoría_id = 1)
    categoria_id = 1
    productos_por_categoria = Producto.objects.raw(
        "SELECT * FROM gestion_producto WHERE categoria_id = %s",
        [categoria_id]
    )

    # RAW 5: Contar productos por categoría manualmente (sin annotate)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.nombre, COUNT(p.id) AS total
            FROM gestion_categoria c
            LEFT JOIN gestion_producto p ON p.categoria_id = c.id
            GROUP BY c.nombre
        """)
        categorias_conteo = cursor.fetchall()

    contexto = {
        'productos_mayor_10000': productos_mayor_10000,
        'productos_ordenados_desc': productos_ordenados_desc,
        'productos_con_categoria': productos_con_categoria,
        'productos_por_categoria': productos_por_categoria,
        'categorias_conteo': categorias_conteo,
    }

    return render(request, "consultas/raw.html", contexto)
