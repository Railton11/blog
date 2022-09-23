from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "name", 
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
        "date_joined",
    )
    fieldsets = (
        (None,{
            "fields":(
                "name",
                "date_joined",
                "birth_date",
                "email",
                "image",
                "password",
            )
        }),
        ("Permissions",{
            "fields":(
                "is_staff",
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        })
    )
    add_fieldsets = (
        (None,{
            "classes": ("wide",),
            "fields": (
                "name",
                "birth_date",
                "email",
                "image",
                "password1",
                "password2",
                "is_active",
                "is_staff",
                "is_superuser"
            )
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
