from datetime import datetime, timedelta

import jwt
from core.models import BaseModel
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import RoleManager


class Roles(models.TextChoices):
    """
    A class that defines the roles that a user can have.
    """

    ADMIN = "ADMIN", "Admin"
    NORMAL_USER = "NORMAL_USER", "Normal User"


class User(AbstractUser, BaseModel, PermissionsMixin):
    """
    Extended user model with additional fields. This is a parent class for all roles.
    """

    user_role = Roles.NORMAL_USER

    role = models.CharField(
        max_length=50,
        choices=Roles.choices,
        default=Roles.NORMAL_USER,
    )
    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name="email address",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.user_role
        return super().save(*args, **kwargs)

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Creates a JSON Web Token with the user's ID and an expiry
        date set to 60 days in the future.
        """
        dt = datetime.now() + timedelta(days=settings.TOKEN_EXPIRY_DAYS)

        return jwt.encode(
            {"id": str(self.pk), "exp": int(dt.timestamp())},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


# Models specific to user roles


# Role: Admin
class Admin(User):
    objects = RoleManager(role=Roles.ADMIN)
    user_role = Roles.ADMIN

    class Meta:
        proxy = True


# Role: NORMAL_USER
class Manager(User):
    objects = RoleManager(role=Roles.NORMAL_USER)
    user_role = Roles.NORMAL_USER

    @property
    def profile(self):
        return self.managerprofile

    class Meta:
        proxy = True
