import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication class for JWT authentication.
    """
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1 or len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY,
                algorithms='HS256'
            )
        except BaseException:
            msg = 'Authentication failed! Bad token.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'User account does not exist!.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'User account has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
