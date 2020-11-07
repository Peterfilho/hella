from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created_at', 'modified_at']
    search_fields = ['name', 'slug']

class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created_at', 'modified_at']
    search_fields = ['name', 'slug', 'category__name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
