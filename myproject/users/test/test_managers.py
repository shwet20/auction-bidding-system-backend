from django.test import TestCase
from users.models import User


class TestUserManger(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email='test@createuser.com',
            password='create_user_password',
        )
        user_db = User.objects.get(id=user.id)
        self.assertEqual(user_db.username, user.username)
        self.assertEqual(user_db.email, user.email)
        self.assertEqual(user_db.username, user.email)
        self.assertEqual(user_db.password, user.password)

    def test_create_user_with_no_email(self):
        with self.assertRaises(TypeError) as context:
            User.objects.create_user(
                username='test_user',
                email=None,
                password='create_user_password',
            )

        self.assertEqual(
            str(context.exception),
            'Users must have an email address.'
        )

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username='test_superuser',
            email='test@createsuperuser.com',
            password='create_superuser_password',
        )
        user_db = User.objects.get(id=user.id)
        self.assertEqual(user_db.username, user.username)
        self.assertEqual(user_db.email, user.email)
        self.assertTrue(user_db.is_superuser)
        self.assertTrue(user_db.is_staff)

    def test_create_superuser_without_password(self):
        with self.assertRaises(TypeError) as context:
            User.objects.create_superuser(
                username='test_superuser',
                email='test@createsuperuser.com',
                password=None
            )

        self.assertEqual(
            str(context.exception).lower(),
            "Superusers must have a password.".lower()
        )
