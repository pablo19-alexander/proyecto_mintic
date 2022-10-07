from rest_framework.routers import DefaultRouter
from .views import ItemView, Tipo_negocioView, UsuarioView, Resultado_clienteView


router = DefaultRouter()

router.register('item', ItemView)
router.register('negocio', Tipo_negocioView)
router.register('usuario', UsuarioView)
router.register('resultado_Cliente', Resultado_clienteView)



urlpatterns = router.urls
