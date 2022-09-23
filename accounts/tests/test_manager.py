from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email = "teste@gmail.com",
            birth_date = "2022-07-21",
            password = "teste123"
        )
        self.assertEqual(user.email, "teste@gmail.com")
        self.assertEqual(user.birth_date, "2022-07-21")
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='super@user.com', 
            birth_date="1964-04-01",
            password="foo123")
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.birth_date, '1964-04-01')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password="foo123", is_superuser=False
            )
