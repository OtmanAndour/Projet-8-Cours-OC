from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('article/<id_article>', views.view_article),
]