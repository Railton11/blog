from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Gerenciador de modelo de usuário personalizado em que o e-mail são os identificadores exclusivos
    para autenticação em vez de nomes de usuário.
    """
    def create_user(self, email, password, **extra_fields):
        "Cria e salva o usuário com email e senha fornecido."
        if not email:
            raise ValueError("O email deve ser definido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        "Cria e salva um super usuário com o email e senha fornecidos."
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_('O usuário deve ter o "is_staff" verdadeiro'))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_('O usuário deve ter o "is_superuser" verdadeiro'))
        return self.create_user(email, password, **extra_fields)