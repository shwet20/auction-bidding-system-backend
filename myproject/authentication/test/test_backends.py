from django.test import TestCase
from rest_framework.test import APIRequestFactory
from users.test.factories import UserFactory
from authentication.backends import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class TestJWTBackend(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.backend = JWTAuthentication()

    def test_authenticate_credentials_method(self):
        request = self.factory.get('/')
        user, token = self.backend._authenticate_credentials(request, self.user.token)

        self.assertEqual(user.id, self.user.id)
        self.assertEqual(token, self.user.token)

    def test_authenticate_credentials_method_with_invalid_token(self):
        request = self.factory.get('/')

        with self.assertRaises(AuthenticationFailed) as context:
            self.backend._authenticate_credentials(request, 'invalid_token')

        self.assertEqual(
            context.exception.detail.lower(),
            'Authentication failed! Bad token.'.lower()
        )

    def test_authenticate_credentials_method_with_user_not_exist(self):
        user = UserFactory()
        token = user.token
        user.delete()
        request = self.factory.get('/')

        with self.assertRaises(AuthenticationFailed) as context:
            self.backend._authenticate_credentials(request, token)

        self.assertEqual(
            context.exception.detail.lower(),
            'User account does not exist!.'.lower()
        )

    def test_authenticate_credentials_method_with_user_not_active(self):
        user = UserFactory(is_active=False)
        request = self.factory.get('/')

        with self.assertRaises(AuthenticationFailed) as context:
            self.backend._authenticate_credentials(request, user.token)

        self.assertEqual(
            context.exception.detail.lower(),
            'User account has been deactivated.'.lower()
        )
