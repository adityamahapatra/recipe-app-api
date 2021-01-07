from typing import Any, Optional

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: Optional[str] = None, **extra_fields: dict[str, Any]
    ):
        if not email:
            raise ValueError("No email specified for the new user")

        """Creates and saves a new user."""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        # ? The kwarg "using=self._db" allows the usage of multiple databases.
        user.save(using=self._db)

        return user

    def create_super_user(self, email: str, password: str):
        """Create and save a new super user."""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
