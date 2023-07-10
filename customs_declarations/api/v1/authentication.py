from rest_framework import authentication
from rest_framework import exceptions

from posting.models import Seller


class ClientIdApiKeyAuthentication(authentication.BaseAuthentication):
    """Аутентификация по Id и Api-key в полях CLIENT_ID и API_KEY."""
    def authenticate(self, request):
        client_id = request.META.get('HTTP_CLIENT_ID')
        api_key = request.META.get('HTTP_API_KEY')
        if not client_id and api_key:
            return None

        try:
            user = Seller.objects.get(client_id=client_id, api_key=api_key)
        except Seller.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
