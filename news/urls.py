from django.urls import path
from news.views import NewsView, SocialView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('socials/', SocialView.as_view(), name='socials')
]