from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description")
    readonly_fields = ("slug",)
    list_filter = ("is_active","is_home",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
