from django.contrib import admin

from .models import News, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "news", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ['aprove_comentario', 'desaprovar_comentario']

    def aprove_comentario(self, request, queryset):
        queryset.update(active=True)

    def desaprovar_comentario(self, request, queryset):
        queryset.update(active=False)
