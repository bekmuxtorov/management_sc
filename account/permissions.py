from rest_framework import permissions
from rest_framework.response import Response
from .models import USER_TYPE


class IsDirectorOrAdminstrator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and (user.type in ['adminstrator', 'director'])):
            return True
        return False


class IsAdminstrator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.type == 'adminstrator'):
            return True
        return False


class IsDirector(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.type == 'director'):
            return True
        return False


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.type == 'teacher'):
            return True
        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if bool(user.is_authenticated and user.type == 'student'):
            return True
        return False
