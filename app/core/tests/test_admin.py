from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        admin_email = "test.super.user@gmail.com"
        email = "test.user@gmail.com"
        password = "testpass123"
        self.admin_user = get_user_model().objects.create_super_user(
            email=admin_email, password=password
        )
        self.client.force_login(user=self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=email, password=password, name="Test User"
        )

    def test_users_listed(self) -> None:
        """Test if users are listed on the user page."""
        url = reverse("admin:core_user_changelist")
        response_ = self.client.get(url)

        self.assertContains(response_, self.user.name)
        self.assertContains(response_, self.user.email)

    def test_user_change_page(self) -> None:
        """Test if the user edit page works."""
        # Sample url: /admin/core/user/1
        url = reverse("admin:core_user_change", args=[self.user.id])
        response_ = self.client.get(url)

        self.assertEquals(response_.status_code, 200)

    def test_create_user_page(self) -> None:
        """Test if the create user page works."""
        url = reverse("admin:core_user_add")
        response_ = self.client.get(url)

        self.assertEquals(response_.status_code, 200)
