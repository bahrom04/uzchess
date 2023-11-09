from rest_framework import serializers
from news.models import News, Socials, ShareButton


class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = ['title', 'image']


class ShareButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareButton
        fields = ['title']


class NewsSerializer(serializers.ModelSerializer):
    socials = SocialsSerializer(many=True)
    share_button = ShareButtonSerializer(many=True)
    
    class Meta:
        model = News
        fields = ['title', 'image', 'content', 'views', 'created_at', 'updated_at']

