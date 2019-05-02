from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    """Exemple de la page non valide au niveau HTML pour que l'exemple soit concis"""
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        return redirect(view_redirection)

    return HttpResponse('Votre article est le n° {0}'.format(id_article))

def view_redirection(request):
    return redirect('afficher_article', id_article=89)

def list_articles(request, month, year):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect("https://www.djangoproject.com")

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def gender(request, sexe):
    sexe = sexe.capitalize()
    return render(request, 'blog/gender.html', locals())

def age(request, age):
    return render(request, 'blog/age.html', locals())
