from django.contrib.auth import get_user_model
from rest_framework import generics, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users import models


User = get_user_model()


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserShortSerializer
    permission_classes = (IsAdmin | IsShopOwner,)

    def get_object(self):
        return self.request.user


class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = User.objects.all()
    lookup_field = "username"


class PhoneRecoveryAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.PhoneRecoverySerializer
    permission_classes = [AllowAny]


class RecoveryVerifyAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.RecoveryVerifySerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        pass


class UserListAPIView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdmin,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdmin,)


class ClientListAPIView(FilterByPermission, generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    search_fields = ("name", "phone_number")
    permission_classes = (IsAdmin | IsShopOwner,)


class ClientDetailView(FilterByPermission, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = (IsAdmin | IsShopOwner,)


class ShopListAPIView(FilterByPermission, generics.ListCreateAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer


class ShopDetailView(FilterByPermission, generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = (IsAdmin | IsShopOwner,)
