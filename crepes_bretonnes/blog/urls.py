from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^accueil', views.home),
    re_path(r'^article/(?P<id_article>.+)', views.view_article),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),
]