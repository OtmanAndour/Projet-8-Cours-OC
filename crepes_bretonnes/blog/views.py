from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import *
from .templatetags import blog_extras
from .forms import *

# Create your views here.

def home(request):
    """Exemple de la page non valide au niveau HTML pour que l'exemple soit concis"""
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    #Puisque l'id n'est plus juste un nombre, mais un nombre attaché avec son slug, il faut 
    #Changer la valeur d'id pour ne garder que le nombre
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


def message(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/message.html', locals())

def add_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'blog/add_article.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    return render(
        request, 
        'blog/voir_contacts.html', 
        {'contacts': Contact.objects.all()}
    )

class FAQView(TemplateView):
    template_name="blog/faq.html"

class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 3

    def get_queryset(self):
       return Article.objects.filter(categorie__id=self.args[0])

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ListeArticles, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories, sans filtre particulier
        context['categories'] = Categorie.objects.all()
        return context

class LireArticle(DetailView):
    context_object_name = "article"
    model = Article
    template_name = "blog/lire.html"

def smart_truncator(request):
    return render(request,'blog/smart_truncator.html')