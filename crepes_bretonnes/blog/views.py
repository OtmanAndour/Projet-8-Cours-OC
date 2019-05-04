from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article

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
def colors(request):
    colors = {
    'FF0000':'red', 
    'ED7F10':'orange', 
    'FFFF00':'yellow', 
    '00FF00':'green', 
    '0000FF':'blue', 
    '4B0082':'indigo', 
    '660099':'purple',
}
    return render(request, 'blog/colors.html', locals())
    
def mypage(request, ID_article):
    return render(request, 'blog/mypage.html', locals()) 

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, "blog/lire.html", {'article':article })