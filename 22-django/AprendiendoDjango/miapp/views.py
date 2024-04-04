from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
<h1>Sitio web con Django | Luis Armando Lira</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de Pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
        <ul>
    """

    year = 2021

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>Hola mundo con Django!</h1>
        <h3>Soy Luis Armando Lira</h3>
    """)

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/contacto/luis armando/lira')
    elif redirigir == 2:
        return redirect('contacto', nombre="Luis", apellidos="lira glez")

    return HttpResponse(layout+'''
        <h1>Página de mi web</h1>
        <p>Creado por Luis Lira</p>
    ''')

def contacto(request,nombre="",apellidos=""):
    html = ""

    if (nombre and apellidos) or nombre:
        html += "<h3>El nombre completo es: </h3>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    return HttpResponse(layout+f'''
        <h2>Contacto</h2>
    '''+html)