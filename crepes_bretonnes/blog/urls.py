from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from .models import Article

urlpatterns = [
    re_path(r'^accueil', views.home),
    re_path(r'^article/(?P<id_article>.+)', views.view_article, name="afficher_article"),
    re_path(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('gender/<sexe>', views.gender),
    path('age/<int:age>', views.age),
    path('colors', views.colors),
    path('mypage/<ID_article>', views.mypage),
    path('message/', views.message, name="message"),
    path('add_article/', views.add_article, name="ajouter_article"),
    path('contact/', views.nouveau_contact, name='nouveau_contact'),
    path('voir_contacts', views.voir_contacts, name="voir_contacts"),
    url(r'^faq$', views.FAQView.as_view()),
    # Nous allons réécrire l'URL de l'accueil
    url(r'^categorie/(\d+)$', views.ListeArticles.as_view(), name="blog_categorie"),
    url(r'^article/(?P<pk>\d+)$', views.LireArticle.as_view(), name='blog_lire'),
    url(r'^truncator', views.smart_truncator, name='smart_truncator')
]