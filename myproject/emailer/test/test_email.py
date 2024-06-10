from django.core import mail
from django.test import TestCase
from emailer.sender import send_signup_success_email
from users.test.factories import UserFactory


class TestEmail(TestCase):

    def setUp(self):
        self.user = UserFactory(email='django-test@mailinator.com')
        self.data = {}

    def test_signup_success_email(self):
        send_signup_success_email(self.user)
        self.assertEqual(len(mail.outbox), 1)
