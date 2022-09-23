from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import (
    authenticate,
    login as login_process,
    logout as logout_process,
    get_user_model
) 
from django.contrib import messages
from django.urls import reverse_lazy
from core import settings
from django.views.generic import FormView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileForm

from .token import generate_token

User = get_user_model()

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        pass1 = request.POST["pass1"]

        user = authenticate(email=email, password=pass1)

        if user is not None:
            login_process(request, user)
            return redirect("index")

        else:
            messages.error(request, "Credenciais ruins.")
            return redirect("login")

    return render(request, "accounts/login.html")

@login_required
def logout(request):
    logout_process(request)
    return redirect("index")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        data = request.POST["data"]
        image = request.POST and request.FILES["image"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(email=email):
                messages.error(request, "email já existe")
                return redirect("register")

        if len(pass1)<8:
            messages.error(request, "Senha deve ter no minimo 8 caracteres")
            return redirect("register")

        if pass1 != pass2:
            messages.error(request, "Senhas incompativeis")
            return redirect("register")
        myuser = User.objects.create_user(name=name, email=email, birth_date=data, image=image, password=pass1)
        myuser.save()

        messages.success(request, "Usuário criado com sucesso, por favor verifique seu email para ativação da conta")

        # E-mail de boas vindas
        subject = "Bem vindo ao Jornal"
        message = "Olá" + "!\n\n" + "Seja bem vindo ao Jornal \n Obrigado por visitar nosso site \n Equipe do jornal"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # E-mail de ativação
        current_site = get_current_site(request)
        email_subject = "Confirme seu e-mail para ativar sua conta!"
        message2 = render_to_string("email_confirmation.html", {
            "name": myuser.name,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(myuser.pk)),
            "token": generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, "accounts/register.html")


@login_required
def profile(request):
    # Salvar alterações
    if request.method == "POST":
        user_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Alterações salvas!")
            return redirect("profile")
    user_form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", context={"user_form": user_form})

class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = "accounts/password.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"Senha atualizada!")
        return super(UpdatePasswordView, self).form_valid(form)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Redefinição de senha solicitada"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": "localhost:8000",
                        "site_name": "JF-News",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            "admin@example.com",
                            [user.email],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse("Erro de cabeçalho encontrado")
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="accounts/password_reset.html",
        context={"password_reset_form": password_reset_form}
    )

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login_process(request, myuser)
        return redirect("index")
    else:
        return render(request, "activate_failed.html")