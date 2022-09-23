from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import (
    IndexListView,
    detail,
    faqs,
    about
)


class TestUrls(SimpleTestCase):
    def test_index(self):
        url = reverse("index")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, IndexListView)

    def test_detail(self):
        url = reverse("detail", args={'slug': "slug"})
        print(resolve(url))
        self.assertEquals(resolve(url).func, detail)

    def test_faqs(self):
        url = reverse("faqs")
        print(resolve(url))
        self.assertEquals(resolve(url).func, faqs)

    def test_about(self):
        url = reverse("about")
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)