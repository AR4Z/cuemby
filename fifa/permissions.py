from django.conf import settings
from rest_framework import exceptions, permissions, status


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if settings.API_KEY_HEADER in request.headers:
            if request.headers[settings.API_KEY_HEADER] == settings.API_KEY:
                return True
            else:
                response = {
                    'message': 'invalid header',
                }

                raise exceptions.PermissionDenied(detail=response,
                    code=status.HTTP_401_UNAUTHORIZED)
        else:
            response = {
                'message': 'missing header',
            }

            raise exceptions.PermissionDenied(detail=response,
                code=status.HTTP_403_FORBIDDEN)
