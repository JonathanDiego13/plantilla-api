from rest_framework import permissions

from commons import token_auth


def _has_token_permission(request):
    if 'HTTP_TOKEN' in request.META:
        return token_auth.token_exists(token=request.META.get('HTTP_TOKEN'))
    return False


class IsTokenAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return _has_token_permission(request=request)


class IsTokenAuthenticatedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method == 'GET' or _has_token_permission(request=request)
