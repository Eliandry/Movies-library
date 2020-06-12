from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.MoviesView.as_view()),
    path('<slug:slug>/',views.MovieDetailView.as_view(),name='movie_detail')
]
