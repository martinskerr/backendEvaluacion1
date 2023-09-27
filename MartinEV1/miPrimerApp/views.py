from django.shortcuts import render

# Create your views here.

def index(request):
    data={
        'nombre':'Martin Patricio',
        'apellido':'Lopez Garrido',
        'profesion':'Estudiante Analista Programador',
        'edad':'20',
        'ciudad':'Talca',
        'imagenPersonal':'https://static.vecteezy.com/system/resources/previews/005/621/014/non_2x/programmer-linear-icon-it-technologist-freelancer-thin-line-illustration-contour-symbol-isolated-outline-drawing-vector.jpg',
    }
    return render(request, 'index.html', data) 

def proyecto1(request):
    data = {
        'nombre': 'Ecommerce Angel Clouds',
        'detalle': 'Plantilla ecommerce, creada para la pyme Angel Clouds. Hecha en totalidad con Html5, Css (Flexbox y Grid), con sistema de agregado de productos al carrito y conectado a una base de datos NOSQL.',
        'cliente': 'Paulina Opazo',
        'anio': '2021',
        'imagen':'https://png.pngtree.com/template/20200707/ourmid/pngtree-angel-wings-logo-vector-modern-simple-clean-designs-with-young-color-image_389363.jpg',
        'link':'https://github.com/martinskerr/AngelClouds-New'
    }
    return render(request, 'proyecto.html', data)

def proyecto2(request):
    data = {
        'nombre': 'Pagina de Cine ',
        'detalle': 'Primer proyecto creado 100% con react, implementado de componentes y sistema backend para el inicio de sesion y compra de boletos',
        'cliente': 'Proyecto Propio',
        'anio': '2021',
        'imagen':'https://img.freepik.com/vector-premium/plantilla-diseno-pagina-destino-sitio-web-vector-entrada-cine_103044-3230.jpg',
        'link':'https://github.com/martinskerr/ticketProProject'
    }
    return render(request, 'proyecto.html', data)

def proyecto3(request):
    data = {
        'nombre': 'Calculadora',
        'detalle': 'Calculadora creada con JavaScript Vanilla, Uso de TailwindCss para la interfaz y Html5',
        'cliente': 'Felipe Catalan',
        'anio': '2022',
        'imagen':'https://img.freepik.com/vector-gratis/diseno-etiqueta-calculadora-aislada_1308-60994.jpg',
        'link':'github.cl/noexiste'
    }
    return render(request, 'proyecto.html', data)