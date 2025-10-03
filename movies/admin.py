from django.contrib import admin
from .models import Movie
from .models import Petition
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)


class PetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'votes_count')
    search_fields = ('title', 'description', 'created_by__username')


admin.site.register(Petition, PetitionAdmin)

