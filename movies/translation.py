from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslation(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslation(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslation(TranslationOptions):
    fields = ('title','tagline','country','description')


