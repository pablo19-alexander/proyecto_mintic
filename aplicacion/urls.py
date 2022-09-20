from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('mas', views.mas, name='mas'),
#----------- cuenta ---------------------------------------
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('mensage', views.registro, name='mensage'),
    path('password', views.password, name='password'), 
    path('correo', views.correo, name='correo'),  
  
    
# ---------- crud -----------------------------------------
    path('crud', views.crud, name='crud'),
    path('crud/crear', views.crear, name='crear'),
    path('crud/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), 
]
