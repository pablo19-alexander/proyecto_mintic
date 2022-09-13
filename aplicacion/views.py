from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
# ----------------paginas priincipales --------------------
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def mas(request):
    return render(request, 'paginas/mas.html')

# ---------- crud -----------------------------------------

def crud(request):#mostramos la lista de requerimientos
    items = Item.objects.all()
    return render(request, 'crud/index.html', {'items': items})

def crear(request):
    formulario = ItemForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('crud')
    return render(request, 'crud/crear.html', {'formulario': formulario})

def editar(request, id):
    item = Item.objects.get(id=id)#obtine el objeto con el id o se hace la cosulta mediante get
    formulario = ItemForm(request.POST or None, request.FILES or None, instance=item)#se la pasamos al formulario
    if formulario.is_valid() and request.POST:#si la informacion es valida y hay un envio 
        formulario.save()# se guardara 
        return redirect('crud')
    return render(request, 'crud/editar.html', {'formulario':formulario})

def eliminar(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('crud')
eliminar