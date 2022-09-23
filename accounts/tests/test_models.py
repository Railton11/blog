from django.test import TestCase

from accounts.models import CustomUser


class TestModels(TestCase):
    def test_data_base(self):
        user = CustomUser.objects.create(
            name = "usuário",
            email = "usuario@gmail.com",
            birth_date = "2022-07-21",
            image = "usuario.png",
        )
        self.assertEqual(user.name, "usuário")
        self.assertEqual(user.email, "usuario@gmail.com")
        self.assertEqual(user.birth_date, "2022-07-21")
        self.assertEqual(user.image, "usuario.png")
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)