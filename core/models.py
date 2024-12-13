from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_approved = models.BooleanField(default=False)
    address = models.TextField(blank=True)  # Dirección del usuario
    phone_number = models.CharField(max_length=20, blank=True)  # Teléfono del usuario
    is_seller = models.BooleanField(default=False)  # Si el usuario es un vendedor

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductFeature(models.Model):
    feature_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.feature_name

class Product(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='available')  # Valor por defecto para el estado
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='products/')
    features = models.ManyToManyField(ProductFeature, related_name="products")  # Características del producto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio
    stock_quantity = models.IntegerField(default=0)  # Cantidad en stock
    description = models.TextField()  # Descripción del producto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Modelos adicionales para Carrito y Pedido

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
