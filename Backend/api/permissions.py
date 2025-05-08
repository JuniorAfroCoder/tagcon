# permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyRequiresAuth(BasePermission):
    """
    Allow POST (create) for everyone.
    Require authentication for GET, LIST, etc.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated
