from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import F
from .forms import ReviewForm, LoginForm, UserRegistrationForm
from django.db import transaction
from .models import Movie, Genre, Session,AgeRating,Reviews

class GenreSidebar:
    """Вывод жанров"""
    def get_genres(self):
        return Genre.objects.all()

class ReviewsSidebar:
    """Вывод отзывов"""
    def get_review(self):
        return Reviews.objects.all()

class FilterMoviesView(GenreSidebar, ListView):
    """Фильтр фильмов"""
    template_name = "siteCin/home.html"
    def get_queryset(self):
        queryset = Movie.objects.filter(Q(genres__in=self.request.GET.getlist("genre"))).distinct()
        return queryset

class ContentCardView(GenreSidebar, ListView):
    """Вывод карточек с фильмами"""
    model = Movie
    queryset = Movie.objects.all()
    template_name = "siteCin/home.html" 

class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""
    template_name = "siteCin/home.html"
    def get_queryset(self):
        #restr = Genre.objects.filter(name)        
        #restriction = Movie.objects.get(genres=restr)    
        queryset = Movie.objects.filter(
            Q(genres__in=self.request.GET.getlist("genre"))
            ).distinct().select_related("restriction").values("id", "title",  "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)

class AddReview(ReviewsSidebar, View):
    """Отзывы"""
    def post(self, request, pk):
        if request.method == "POST":           
            form = ReviewForm(request.POST)
            movie = Movie.objects.get(id=pk)
            if form.is_valid():
                form = form.save(commit=False)
                form.movie = movie                           
                form.save()
                transaction.commit() 
            return redirect(movie.get_absolute_url())
        else:
            form = ReviewForm()
            transaction.rollback()



class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['session_list']  = Session.objects.filter(movie=self.object).distinct()
        return context


def register(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})



'''
context['session_list']  = Session.objects.filter(movie=self.object).order_by('date').distinct().group_by('hall')

movie__id=F('movie')
movie__title=self.request.GET.get("url")
class ContentView(ListView):
    """docstring for ContentView"""
    model = Genre
    queryset = Genre.objects.all()
    template_name = "siteCin/home.html"
    #return render(request, 'siteCin/home.html', {'genre_list':genres})

class ContentCardView(View):
    def get(self,request):
        movies = Movie.objects.all()
        return render(request, 'siteCin/home.html', {'card_list':movies})
'''

        