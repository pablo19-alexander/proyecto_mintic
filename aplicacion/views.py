from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
# ----------------paginas priincipales -------------------
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def mas(request):
    return render(request, 'paginas/mas.html')

#----------- cuenta ---------------------------------------

def registro(request):
    contexto = dict()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(
                username = email,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            messages.success(request, '¡¡Te has registrado exitosamente!!')
            return redirect('login')
        else:
            messages.error(request, '¡¡Error al registrar el usuario!!')
            return redirect('registro')
    else:
        user = UserForm()
        contexto['userform'] = user
        return render(request, 'cuenta/registro.html', contexto)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)       
            if user is not None:
                login(request, user)
                return redirect(reverse('inicio'))
            else:
                messages.error(request, '¡¡Las credenciales no son correctas!!')
                return redirect(reverse('login'))
        else:
            messages.error(request, '¡¡Verifique los datos ingresado!!')
            return redirect(reverse('login'))
    else:
        form = LoginForm()
        return render(request, 'cuenta/login.html', {'form': form})
    
#----------- contraseña ---------------------------------------    
def password(request):
    return render(request, "cuenta/password.html")

def correo(request):
    return render(request, "cuenta/correo.html")

def logout_user(request):
    logout(request)
    return redirect(reverse('inicio'))

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



