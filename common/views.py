from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from common.models import Favourite
from common.serializerls import FavouriteSerializer
from common.utils import get_knox_auth_urls
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class FavouriteListView(generics.ListAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user_name = self.kwargs['user_name']
        user = User.objects.get(username=user_name)

        return Favourite.objects.filter(user=user).prefetch_related('favourites')


    def list(self, request, *args, **kwargs):
        auth_urls = get_knox_auth_urls()

        return JsonResponse({
            'auth_urls': auth_urls,
            'data': FavouriteSerializer(self.get_queryset(), many=True).data
        })

    
    