from rest_framework import serializers
from news.models import News, Socials


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = ['title', 'image']


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = [
            'id',
            'title', 
            'image', 
            'content', 
            'views', 
            'created_at', 
            'updated_at',
            ]

