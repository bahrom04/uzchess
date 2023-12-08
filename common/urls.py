from django.urls import path
from common.views import FavouriteListView


urlpatterns = [
    path('<slug:user_name>/favourite/', FavouriteListView.as_view(), name='user_favourite')
]