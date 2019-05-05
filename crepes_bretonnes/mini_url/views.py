from django.shortcuts import render, redirect, get_object_or_404
from mini_url.models import *
from .forms import *


def home(request):
    urls = MiniURL.objects.order_by('-acces')
    return render(request,'mini_url/home.html', locals())

def redirection(request, code):
    page = get_object_or_404(MiniURL, code=code)
    page.acces += 1
    page.save()
    return redirect(page.url, permanent=True)

def create_mini_url(request):
    form = MiniURLForm(request.POST or None)
    envoi = False
    if form.is_valid():
        envoi = True
        form.save()
    return render(request, 'mini_url/create_mini_url.html', locals())
