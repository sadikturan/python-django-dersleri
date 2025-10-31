from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    # readonly_fields = ("description")

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
