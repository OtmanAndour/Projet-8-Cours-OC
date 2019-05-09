from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^test/', views.test_i18n, name="test"),
    url(r'^translation', TemplateView.as_view(template_name='i18n/translation.html')),
]