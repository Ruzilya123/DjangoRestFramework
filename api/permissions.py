from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view): # Проверка на права доступа
        return request.user.is_staff
    
class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
  
class IsGuest(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated