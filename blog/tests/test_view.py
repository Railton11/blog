from django.test import TestCase, Client
from django.urls import reverse

from blog.models import News
from accounts.models import CustomUser

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse("index")
        self.detail_url = reverse("detail", args=['noticia'])
        self.faqs_url = reverse("faqs")
        self.about_url = reverse("about")

        self.user = CustomUser.objects.create_user(
            name="Lucas",
            birth_date="2000-08-18",
            email="teste@teste.com",
            password="teste@Lucas123"
        )

        self.noticia = News.objects.create(
            slug = 'noticia',
            author = self.user
        )

    def test_context_index_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_context_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/detail.html")

    def test_faqs_GET(self):
        response = self.client.get(self.faqs_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/faqs.html")

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/about.html")