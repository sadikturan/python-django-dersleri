from django.contrib import admin
from .models import Address, Category, Product, Supplier

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","slug","selected_categories",)
    list_display_links = ("name","price")
    prepopulated_fields = { "slug": ("name",) }
    list_filter = ("name","price","categories")
    list_editable = ("isActive",)
    search_fields = ("name","description")

    def selected_categories(self, obj):
        html = ""

        for category in obj.categories.all():
            html += category.name + " "

        return html    

    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Address)