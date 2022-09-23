from tabnanny import verbose
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField("Título", max_length=80, help_text="Máximo de 80 caracteres.")
    slug = models.SlugField(
        "Identificador",
        max_length=50,
        help_text="Máximo de 50 caracteres.",
        unique=True,
        error_messages={
            "unique":"Um identificador como este já existe."
        }
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor")
    body = RichTextUploadingField("Escopo", help_text="Discorra seu texto aqui")
    #body = models.TextField("Escopo")
    created = models.DateTimeField("Criado", auto_now_add=True)
    update = models.DateTimeField("Modificado", auto_now=True)
    image = models.ImageField("Capa", upload_to="noticias", help_text="Permitido apenas imagem")
    video = models.FileField("Video", upload_to="video-das-noticias", blank=True, null=False, help_text="Permitido apenas vídeos")
    description = models.CharField("Descrição", max_length=100, help_text="Máximo de 100 caracteres.")
    tags = TaggableManager()

    class Meta:
        ordering = ("-created",)
        verbose_name = "Notícia"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments", verbose_name="Noticia", help_text="Escolha a postagem")
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Autor", help_text="Autor do comentário")
    body = models.TextField(verbose_name="comentários")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    active = models.BooleanField(default=False, verbose_name="Aprovado", help_text="Analise o texto para ser exibido na postagem")

    class Meta:
        ordering = ["created_on",]
        verbose_name = "comentário"

    def __str__(self):
        return 'Comentários {} de {}'.format(self.body, self.name)

