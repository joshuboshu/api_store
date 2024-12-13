from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, ProductViewSet, CategoryViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
