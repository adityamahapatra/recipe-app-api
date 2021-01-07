from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self) -> None:
        """Test if creating a new user with an email is successful."""
        email = "test.user@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self) -> None:
        """Test if the email for a new user is normalized."""
        email = "test.user@GMAIL.COM"
        user = get_user_model().objects.create_user(email=email, password="testpass123")

        self.assertEquals(user.email, email.lower())

    def test_new_user_email_validity(self) -> None:
        """Test if creating a new user without an email raises an error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="testpass123")

    def test_create_new_super_user(self) -> None:
        """Test creating a new super user."""
        email = "test.super.user@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_superuser(
            email=email, password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
