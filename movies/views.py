from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
from django.http import HttpResponseRedirect


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)

    # def get_context_data(self, **kwargs):
    # context = super(MoviesView, self).get_context_data(**kwargs)
    # context['categories'] = Category.objects.all()
    # return context


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        text = request.POST.get('textcomm')
        name = request.POST.get('namecomm')
        email = request.POST.get('emailcomm')
        parent = None
        if request.POST.get('parent', None):
            parent = int(request.POST.get('parent'))
        review = Reviews(name=name, email=email, text=text, movie=movie, parent_id=parent)
        review.save()
        return HttpResponseRedirect(movie.get_absolute_url())


class ActorView(DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"