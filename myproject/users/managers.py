from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class RoleManager(models.Manager):
    """
    Model manager class to filter the queryset by role
    """

    def __init__(self, role):
        self.role = role
        super().__init__()

    def get_queryset(self):
        return super().get_queryset().filter(role=self.role)


class UserManager(BaseUserManager):
    use_in_migrations = True

    """
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, email, username=None, password=None):
        """
        Create and return a `User` with an email and password.
        """

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=self.normalize_email(email),
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
