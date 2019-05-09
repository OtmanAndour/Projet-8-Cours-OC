from django.conf.urls import url
from . import views

urlpatterns = [
    # Une string vide indique la racine
    url(r'^$', views.liste, name='url_liste'),
    url(r'^(?P<page>\d+)$', views.liste, name='url_liste'),
    url(r'^nouveau$', views.URLCreate.as_view(), name='url_nouveau'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques. 
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
    url(r'^edition/(?P<code>\w{6})$', views.URLUpdate.as_view(), name='url_update'),
    url(r'^supprimer/(?P<code>\w{6})$', views.URLDelete.as_view(), name='url_delete'),
]