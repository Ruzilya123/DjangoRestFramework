from rest_framework.permissions import BasePermission
from typing import Any

class GroupPermission(BasePermission):
    def __init__(self, group_name: list):
        self.group_name = group_name
      
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.groups.filter(name__in=self.group_name).exists()
        return False