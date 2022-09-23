from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q

from .models import News, Comment
from .form import CommentForm


class IndexListView(ListView):
    model = News
    template_name = "blog/index.html"
    context_object_name = "context"
    paginate_by = 9

    def get_queryset(self):
        context = News.objects.all()
        q = self.request.GET.get('research', None)

        if q is not None:
            context = context.filter(
                Q(tags__name__icontains=q) |
                Q(title__icontains=q)
            )
        return context

def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    comments = Comment.objects.filter(active=True, news=news)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(
        request,
        "blog/detail.html",
        {
            "news": news,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        }
    )

def faqs(request):
    return render(request, "blog/faqs.html")

def about(request):
    return render(request, "blog/about.html")
