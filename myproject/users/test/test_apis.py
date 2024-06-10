from django.conf import settings
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from users.api.views import UserGetUpdateView
from users.test.factories import UserFactory


class TestGetAndUpdateUserAPI(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.endpoint = settings.API_PREFIX + '/users/'
        self.user = UserFactory()
        self.auth_token = "token {}".format(self.user.token)

    def test_get_user_success(self):
        request = self.factory.get(self.endpoint, HTTP_AUTHORIZATION=self.auth_token)
        response = UserGetUpdateView.as_view()(request)
        expected_response = {
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'token': self.user.token,
        }
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, expected_response)

    def test_unauthorised_user_cannot_access_user_data(self):
        request = self.factory.get(self.endpoint)
        response = UserGetUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 403)

    def test_user_can_update_email(self):
        request = self.factory.patch(
            self.endpoint,
            {'email': 'test2@example.com'},
            HTTP_AUTHORIZATION=self.auth_token
        )
        response = UserGetUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], 'test2@example.com')

    def test_user_can_update_password(self):
        request = self.factory.patch(
            self.endpoint,
            {'password': 'Test@123'},
            HTTP_AUTHORIZATION=self.auth_token
        )
        response = UserGetUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_unauthorised_user_cannot_update_user_data(self):
        request = self.factory.patch(
            self.endpoint,
            {'email': 'test2@example.com'}
        )
        response = UserGetUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 403)
