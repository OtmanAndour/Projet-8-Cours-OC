from django.urls import path, re_path
from . import views

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
]