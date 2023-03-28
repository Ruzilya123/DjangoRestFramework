from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.use.user_group.name == 'client'
  
class IsGuest(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.use.user_group.name == 'guest'
    
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.use.user_group.name == 'admin'