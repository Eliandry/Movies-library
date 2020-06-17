from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *
from django.utils.safestring import mark_safe

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())


    class Meta:
        model = Movie
        fields = '__all__'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}


class ReviewFilm(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ('name', 'email')


class ShotsFilm(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" ')

    get_image.short_description = "Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft','get_poster')
    prepopulated_fields = {'url': ('title',)}
    list_filter = ('year',)
    readonly_fields = ('get_poster',)
    search_fields = ('title',)
    inlines = [ShotsFilm, ReviewFilm]
    save_on_top = True
    list_editable = ('draft',)
    form = MovieAdminForm
    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50"')

    get_poster.short_description = "Постер"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Фото"


admin.site.register(Rating)
admin.site.register(RatingStar)


@admin.register(MovieShots)
class ShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'movie', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.site_title = "Films administration"
admin.site.site_header = "Films administration"
