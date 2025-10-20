from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","slug",)
    list_display_links = ("name","price")
    prepopulated_fields = { "slug": ("name",) }
    list_filter = ("name","price",)
    list_editable = ("isActive",)
    search_fields = ("name","description")

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)