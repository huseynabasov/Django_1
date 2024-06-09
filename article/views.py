from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.urls import reverse
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return render(request, "index.html")


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")


@login_required(login_url="account:login")
def articles__view(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all()
    return render(request, "articles.html", {"articles": articles})


@login_required(login_url="account:login")
def dashboard__view(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, "dashboard.html", {"articles": articles})


@login_required(login_url="account:login")
def addarticle__view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save()

        messages.success(request, "Meqaleniz ugurla elave edildi...")
        return redirect("dashboard")
    context = {"form": form}

    return render(request, "addarticle.html", context)


@login_required(login_url="account:login")
def article__update__view(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save()

        messages.success(request, "Meqaleniz ugurla elave guncellendi...")
        return redirect("dashboard")
    context = {"form": form}

    return render(request, "update.html", context)


@login_required(login_url="account:login")
def article__delete__view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Meqaleniz ugurla silindi...")
    return redirect("dashboard")
    pass


@login_required(login_url="account:login")
def article__detail__view(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(article=article)
    context = {"article": article, "comments": comments}
    return render(request, "article-detail.html", context)


@login_required(login_url="account:login")
def addcomment_view(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(
            comment_author=comment_author, comment_content=comment_content
        )

        newComment.article = article
        newComment.save()
        messages.success(request, "Serhiniz ugurla elave edilmisdir....")

    return redirect(reverse("article-detail", kwargs={"id": id}))
