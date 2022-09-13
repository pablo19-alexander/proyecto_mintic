from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('mas', views.mas, name='mas'),
    
# ---------- crud -----------------------------------------
    path('crud', views.crud, name='crud'),
    path('crud/crear', views.crear, name='crear'),
    path('crud/editar', views.editar, name='editar'),
    
]
