from rest_framework.permissions import BasePermission

class GroupPermission(BasePermission):
    def __init__(self, group_name: list):
        self.group_names = group_name

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.groups.filter(name__in=self.group_name).exists()
        return False