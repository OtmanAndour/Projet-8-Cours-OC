from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('create_mini_url', views.create_mini_url, name="create_mini_url"),
    path('redirection/<code>', views.redirection, name="redirection")
]