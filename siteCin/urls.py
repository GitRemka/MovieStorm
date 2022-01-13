from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.ContentCardView.as_view(), name='home'), 
    path('filter/', views.FilterMoviesView.as_view(), name='filter'), 
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path('accounts/', include('allauth.urls')),
]