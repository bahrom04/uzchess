from django.contrib import admin
from common.models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user']
    ordering = ['user']



admin.site.register(Favourite, FavouriteAdmin)
