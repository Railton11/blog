from django.urls import path

from .views import (
   login,
   logout,
   register,
   profile,
   UpdatePasswordView,
   password_reset_request,
   activate
)

urlpatterns = [
    path("", login, name="login"),
    path("register/", register, name="register"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("update-password/", UpdatePasswordView.as_view(), name="password"),
    path("password-reset/", password_reset_request, name="password_reset"),
    
]