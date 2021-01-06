from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test if creating a new user with an email is successful."""
        email = "test.user@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the email for a new user is normalized."""
        email = "test.user@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email, password="testpass123"
        )

        self.assertEquals(user.email, email.lower())
