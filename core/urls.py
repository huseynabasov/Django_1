"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("articles/", articles__view, name="articles"),
    path("article-detail/<int:id>", article__detail__view, name="article-detail"),
    path("dashboard/", dashboard__view, name="dashboard"),
    path("addarticle/", addarticle__view, name="addarticle"),
    path("update/<int:id>", article__update__view, name="update"),
    path("delete/<int:id>", article__delete__view, name="delete"),
    path("comment/<int:id>", addcomment_view, name="comment"),
    path("addcomment_view/", include("account.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("admin/", admin.site.urls),
]


# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)