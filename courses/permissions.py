from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.request import Request
from rest_framework.views import APIView


class CustomAccessPermission(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        # admin_methods = ("POST","DELETE")

        if request.method == "GET":
            return True

        elif request.method == "POST":
            return request.user and IsAdminUser().has_permission(request, view)

        elif request.method == "DELETE":
            return request.user and IsAdminUser().has_permission(request, view)

        else:
            return False


class IsOwnerOfObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id
