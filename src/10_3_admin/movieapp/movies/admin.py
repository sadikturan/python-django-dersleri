from django.contrib import admin

from movies.models import Contact, Genre, Movie, Person, Video

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Genre)
admin.site.register(Video)
