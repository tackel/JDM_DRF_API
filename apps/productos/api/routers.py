from rest_framework.routers import DefaultRouter
from apps.productos.api.viewset.product_viewset import ProductViewSet
router = DefaultRouter()

router.register(r'productos', ProductViewSet, basename='productos')

urlpatterns = router.urls