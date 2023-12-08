from rest_framework import serializers
from common.models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = (
            'id',
            'user',
            'book',
            'course'
        )