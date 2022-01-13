from django.contrib import admin
from .models import Actor, Genre, Country,Format, AgeRating, Movie, Session,Ticket,Profile,PlaceAndRow,Hall,FormatHall,Reviews

admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Format)
admin.site.register(AgeRating)
admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Ticket)
admin.site.register(Profile)
admin.site.register(PlaceAndRow)
admin.site.register(Hall)
admin.site.register(FormatHall)
admin.site.register(Reviews)