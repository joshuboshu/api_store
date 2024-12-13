from django.contrib import admin
from .models import User, Product, Category, ProductFeature

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_approved', 'date_joined']  # Añadido 'date_joined'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'created_at', 'updated_at']  # Agregados 'created_at' y 'updated_at'
    list_filter = ['status', 'created_at']  # Filtro por 'status' y 'created_at'
    search_fields = ['name', 'status']  # Búsqueda por 'name' y 'status'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # No requiere cambios

@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ['feature_name', 'description']
