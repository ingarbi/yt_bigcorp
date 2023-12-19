from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',),
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand',  'price', "discount",
                    'available', 'created_at', 'updated_at')
    list_filter = ('available', 'created_at', 'updated_at')
    ordering = ('title',)

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',),
        }
