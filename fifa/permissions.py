from django.conf import settings
from rest_framework import exceptions, permissions, status


class CustomPermission(permissions.BasePermission):
    """Subclass for custom authorization in endpoints using x-api-key http header
    """
    def has_permission(self, request, view):
        if settings.API_KEY_HEADER in request.headers:
            if request.headers[settings.API_KEY_HEADER] == settings.API_KEY:
                return True

            response = {
                'message': 'invalid header',
            }

            raise exceptions.PermissionDenied(detail=response,
                code=status.HTTP_401_UNAUTHORIZED)
        response = {
            'message': 'missing header',
        }

        raise exceptions.PermissionDenied(detail=response,
            code=status.HTTP_403_FORBIDDEN)
