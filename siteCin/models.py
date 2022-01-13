from django.db import models
from django.conf import settings
from datetime import time, date
from django.urls import reverse
from django.db.models.query import QuerySet
from django_group_by import GroupByMixin

class BookQuerySet(QuerySet, GroupByMixin):
    pass

class Actor(models.Model):
    """Актеры"""
    name = models.CharField("Имя", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"
        ordering = ('name',)

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Название жанра", max_length=100)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

class Country(models.Model):
    """Страны"""
    country = models.CharField("Страны", max_length=100)
    
    def __str__(self):
        return self.country
    
    class Meta: 
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ('country',)

class Format(models.Model):
    """Форматы фильмов"""
    name = models.CharField("Название формата", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы'
        ordering = ('name',)

class AgeRating(models.Model):
    """Возрастной рейтинг"""
    name = models.CharField("Возрастной рейтинг", max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастные рейтинги'
        ordering = ('name',)

class Movie(models.Model):
    """Фильмы"""
    title = models.CharField("Название", max_length=100)
    director = models.CharField("Режиссер", max_length=100)
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    date = models.DateField("Дата выхода", default=date.today)
    duration = models.TimeField("Длительность")
    rating = models.FloatField("Рейтинг", default=0)
    restriction = models.ForeignKey(
        AgeRating, verbose_name="Возрастной рейтинг", on_delete=models.SET_NULL,null=True
    )
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="Указать сумму в долларах")
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="images/")
    poster_2 = models.ImageField("Постер_2", upload_to="images/", default=1)
    genres = models.ManyToManyField(Genre,verbose_name="Жанры")
    countrys = models.ManyToManyField(Country,verbose_name="Страны")
    #formats = models.ManyToManyField(Format,verbose_name="Форматы")
    url = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)
    
    class Meta: 
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('-date',)

class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.name} - {self.movie}"
    
    def get_absolute_url(self):
        return reverse("home", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.all()
    
    class Meta: 
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Hall(models.Model):
    """Залы"""
    name = models.CharField("Наименование", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'
        ordering = ('name',)

class Session(models.Model):
    """Сеансы"""
    objects = BookQuerySet.as_manager()
    movie = models.ForeignKey(Movie, verbose_name="Фильм",on_delete=models.CASCADE)    
    format = models.ForeignKey(Format, verbose_name="Формат",on_delete=models.CASCADE,default=1)
    hall = models.ForeignKey(Hall, verbose_name="Зал", on_delete=models.CASCADE)
    date = models.DateField("Дата сеанса", default=date.today)
    time = models.TimeField("Время")
    cost = models.PositiveSmallIntegerField("Стоимость", default=0, help_text="Указать сумму в рублях")
    
    def __str__(self):
        return str(self.movie)
    
    class Meta: 
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
        ordering = ('movie',)

class PlaceAndRow(models.Model):
    """Места и ряды"""
    hall = models.ForeignKey(Hall, verbose_name="Зал", on_delete=models.CASCADE)
    row = models.PositiveSmallIntegerField("Ряд", default=0)
    place = models.PositiveSmallIntegerField("Место", default=0)

    def __str__(self):
        return str(self.hall)
    
    class Meta: 
        verbose_name = 'Место и ряд'
        verbose_name_plural = 'Места и ряды'

class Profile(models.Model):
    """Профиль"""
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    date_birth = models.DateField("Дата рождения", default=date.today)
    gender = models.CharField("Пол",max_length=10) 
    email = models.EmailField()
    phone = models.CharField("Телефон", max_length=50)
    wishes = models.TextField("Пожелания", max_length=5000)

    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Ticket(models.Model):
    """Билеты"""
    session = models.ForeignKey(Session, verbose_name="Сеанс",on_delete=models.DO_NOTHING)
    place = models.ForeignKey(PlaceAndRow, verbose_name="Место и ряд", on_delete=models.DO_NOTHING)
    date_sale = models.DateField("Дата продажи", default=date.today) 
    paid = models.BooleanField("Оплачено", default=False)  
    user = models.ForeignKey(Profile, verbose_name="Профиль",on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.session
    
    class Meta: 
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

class FormatHall(models.Model):
    """Форматы_Залы"""
    hall = models.ForeignKey(Hall, verbose_name="Зал", on_delete=models.CASCADE)
    formats = models.ManyToManyField(Format,verbose_name="Форматы")
    
    def __str__(self):
        return str(self.hall)

    class Meta: 
        verbose_name = 'Формат_Зал'
        verbose_name_plural = 'Форматы_Залы'
        ordering = ('hall',)
        
        
