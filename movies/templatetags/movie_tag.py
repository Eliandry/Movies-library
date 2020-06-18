from django import template
from ..models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_film.html')
def get_last_movies(count=4):
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': movies}
