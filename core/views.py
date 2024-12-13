from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User, Product, Category, ProductFeature, Cart, CartItem, Order, OrderItem
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ProductFeatureSerializer, CartSerializer, OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'status', 'categories']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            user = self.request.user
            if not user.is_authenticated or not user.is_approved:
                self.permission_denied(self.request, message="No tienes permiso para realizar esta acción.")
        return []

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProductFeatureViewSet(viewsets.ModelViewSet):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer
    permission_classes = [IsAuthenticated]

# Vistas para Carrito y Pedido

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
