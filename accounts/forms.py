from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("Um usuário com esse e-mail já existe")
        return self.cleaned_data['email']
    
    class Meta:
        model = CustomUser
        fields = ("name", "email", "birth_date", "image", "password1", "password2")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
        

class ProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("name", "birth_date", "image",)


class PasswordForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("password",)
