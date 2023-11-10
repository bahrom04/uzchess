from django.contrib import admin
from .models import User, FavouriteBook, FavouriteCource

admin.site.register(User)
admin.site.register(FavouriteBook)
admin.site.register(FavouriteCource)

