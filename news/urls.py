from django.urls import path
from news.views import SocialView, NewsListView, NewsDetailView


urlpatterns = [

    path('socials/', SocialView.as_view(),),
    path('news/', NewsListView.as_view()),
    path('news/<int:id>', NewsDetailView.as_view())


]