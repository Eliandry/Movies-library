from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}


class ReviewFilm(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    prepopulated_fields = {'url': ('title',)}
    list_filter = ('year',)
    search_fields = ('title',)
    inlines = [ReviewFilm]
    save_on_top = True
    list_editable = ('draft',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email')


admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(MovieShots)
