from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("nome"), max_length=80, help_text="Apenas é permitido 80 caracteres.")
    email = models.EmailField(
        _("endereço de e-mail"), unique=True, max_length=256, error_messages={
            "unique":"Um usuário com este email já existe."
            
        },help_text="Requeridos. 256 caracteres ou menos. Apenas letras, dígitos e +/-/_.")
    birth_date = models.DateField(_("data de nascimento"), null=False)
    image = models.ImageField(_("imagem"), upload_to="usuarios")
    is_active = models.BooleanField(_("ativo"), default=False)
    is_staff = models.BooleanField(_("equipe"), default=False)
    is_superuser = models.BooleanField(_("administrador"), default=False)
    date_joined = models.DateTimeField(_("data de ingresso"), default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["birth_date"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Usuário"

    def __str__(self):
        return self.name
