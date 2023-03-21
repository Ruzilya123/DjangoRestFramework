from rest_framework.permissions import BasePermission, SAFE_METHODS

class isAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff and request.user or request.method in SAFE_METHODS)
