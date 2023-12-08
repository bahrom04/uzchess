from django.urls import path, include
from news.views import NewsView, SocialView


urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('socials/', SocialView.as_view(), name='socials'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

