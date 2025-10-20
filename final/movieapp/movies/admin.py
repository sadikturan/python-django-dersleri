from django.contrib import admin

from movies.models import Comment, Contact, Genre, Movie, Person, Slider, Video

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','is_home',)
    prepopulated_fields = {'slug': ('title',) }
    list_filter = ('genres','language','is_active','is_home',)
    search_fields = ('title','description',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name','gender','duty_type')
    list_filter = ('gender','duty_type')
    search_fields = ('first_name','last_name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name','movie',)
    list_filter = ('full_name','movie',)
    search_fields = ('movie__title','text')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
admin.site.register(Slider)
admin.site.register(Comment, CommentAdmin)
