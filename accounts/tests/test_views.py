from django.test import TestCase, Client
from django.urls import reverse
from PIL import Image
import tempfile

from accounts.models import CustomUser


# Cria uma imagem temporário
def temporary_image():
        
    image = Image.new("RGB", (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg", prefix="test_img_")
    image.save(tmp_file, "jpeg")
    tmp_file.seek(0)
    return tmp_file


class TestViewsAccounts(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.register_url = reverse("register")
        self.profile_url = reverse("profile")
        self.updatepassword_url = reverse("password")
        self.about_url = reverse("about")
        self.user = CustomUser.objects.create_user(
            name="Lucas",
            birth_date="2000-08-18",
            email="teste@teste.com",
            password="teste@Lucas123"
        )
    

    def test_view_logi_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")

    def test_view_login_post(self):
        response = self.client.post(self.login_url,{
            "email": self.user.email,
            "pass1": self.user.password
        })
        self.assertEqual(response.status_code, 302)
    
    def test_view_register_get(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_view_login_post(self):
        response = self.client.post(self.register_url,{
            "name": "Maria",
            "email": "maria@gmail.com",
            "data": "1999-05-15",
            "image": temporary_image(),
            "pass1": "maria22@10maria",
            "pass2": "maria22@10maria"
        })
        self.assertEqual(response.status_code, 302)

    def test_view_profile_post(self):
        response = self.client.post(self.profile_url,{
            "name": "Maria da gloria",
            "birth_date": "1998-08-17",
            "image": temporary_image()
        })
        self.assertEqual(response.status_code, 302)

    def test_view_update_password_post(self):
        response = self.client.post(self.updatepassword_url,{
            "pass1": "password123",
            "pass2": "password123"
        })
        self.assertEquals(response.status_code, 302)

    def test_view_about_get(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
