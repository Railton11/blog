from django.urls import path

from .views import IndexListView, detail, faqs, about

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("common-questions", faqs, name="faqs"),
    path("about", about, name="about"),
    path("<slug:slug>", detail, name="detail"),
]
