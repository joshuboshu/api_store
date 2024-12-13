from rest_framework import serializers
from .models import User, Product, Category, ProductFeature, Cart, CartItem, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_approved', 'address', 'phone_number', 'is_seller']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'feature_name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    features = ProductFeatureSerializer(many=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'status', 'categories', 'image', 'features', 'price', 'stock_quantity', 'description', 'created_at', 'updated_at']

# Serializadores para Carrito y Pedido

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total', 'shipping_address', 'created_at', 'items']
