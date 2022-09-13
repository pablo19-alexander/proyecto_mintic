from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# ----------------paginas priincipales --------------------
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def mas(request):
    return render(request, 'paginas/mas.html')

# ---------- crud -----------------------------------------

def crud(request):
    return render(request, 'crud/index.html')

def crear(request):
    return render(request, 'crud/crear.html')

def editar(request):
    return render(request, 'crud/editar.html')
