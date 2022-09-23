from django.test import TestCase
from django.contrib.auth import get_user_model

from blog.models import News, Comment
from accounts.models import CustomUser


class TestModelsBlog(TestCase):
    def test_models_news(self):

        news = News.objects.create(
            title = "noticia",
            slug = "noticia",
            author = CustomUser.objects.create_user(
                email = "teste@gmail.com",
                birth_date = "2022-07-21",
                password = "teste123"
            ),
            body = "noticia do dia",
            image = "imagem.png",
            video = "video.mp4",
            description = "tests de noticia"
        )
        self.assertEqual(news.title, "noticia")
        self.assertEqual(news.slug, "noticia")
        self.assertEqual(news.body, "noticia do dia")
        self.assertEqual(news.image, "imagem.png")
        self.assertEqual(news.video, "video.mp4")
        self.assertEqual(news.description, "tests de noticia")