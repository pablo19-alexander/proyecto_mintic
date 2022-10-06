from django.urls import path
from . import views

urlpatterns = [
#----------- paginas principales -------------------------
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('mas', views.mas, name='mas'),
# ---------- formularios ----------------------------------
    path('formulario', views.formulario, name='formulario'),
    path('formulario_res', views.formulario_res, name='formulario_res'),
    path('formulario_dro', views.formulario_dro, name='formulario_dro'),
#----------- cuenta ---------------------------------------
    path('registro', views.registro, name='registro'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('mensage', views.registro, name='mensage'),
# ---------- crud -----------------------------------------
    path('crud', views.crud, name='crud'),
    path('crud/crear', views.crear, name='crear'),
    path('crud/editar/<int:id>', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'), 
]
