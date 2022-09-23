from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import (
    login,
    logout,
    register,
    profile,
    UpdatePasswordView,
    password_reset_request,
    activate
)

from accounts import token


class TestUrls(SimpleTestCase):
    def test_login_url(self):
        url = reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_logout_url(self):
        url = reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout)
    
    def test_register_url(self):
        url = reverse("register")
        print(resolve(url))
        self.assertEquals(resolve(url).func, register)

    def test_profile_url(self):
        url = reverse("profile")
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)

    def test_update_password_view_url(self):
        url = reverse("password")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, UpdatePasswordView)

    def test_password_reset_request_url(self):
        url = reverse("password_reset")
        print(resolve(url))
        self.assertEquals(resolve(url).func, password_reset_request)

    def test_activate_url(self):
        url = reverse("activate", args={'uidb64': 'uidb64', 'token': 'token'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, activate)
