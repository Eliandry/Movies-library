from django.db.models import Q
from .forms import RatingForm, ReviewForm
from django.views.generic import ListView, DetailView, View
from .models import *
from django.http import HttpResponseRedirect, HttpResponse


class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        years_sorted_list = sorted(set(Movie.objects.filter(draft=False).values_list('year', flat=True)))
        return years_sorted_list


class MoviesView(GenreYear, ListView):
    paginate_by = 1
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['form']=ReviewForm()
        return context


class AddReview(GenreYear, View):
    def post(self, request, pk):
        form  = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return HttpResponseRedirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):
    paginate_by = 1

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre")) |
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct().values("title", "tagline", "url", "poster")
        return queryset

    def get_context_data(self, **kwargs):
        context = super(FilterMoviesView, self).get_context_data(**kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context


class AddStarRating(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class SearchView(GenreYear, ListView):
    paginate_by = 4
    def get_queryset(self):
        title= self.request.GET.get("q")
        return Movie.objects.filter(title=title)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context