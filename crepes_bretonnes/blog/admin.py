from django.contrib import admin
from django.utils.text import Truncator

from .models import Categorie, Article


class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'auteur', 'date', 'apercu_contenu')
   list_filter    = ('auteur','categorie',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('titre', 'contenu')

   def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article, 
        suivi de points de suspension si le texte est plus long. 
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    # En-tête de notre colonne
   apercu_contenu.short_description = "Aperçu du contenu"

   fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
   ('Général', {
        'classes': ['collapse',],
        'fields': ('titre', 'auteur', 'categorie')
    }),
    # Fieldset 2 : contenu de l'article
    ('Contenu de l\'article', {
       'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
       'fields': ('contenu', )
    }),
)
   #Erreur lors du prepopulated: Slug key is not found 
   #prepopulated_fields = {'slug': ('titre', ), }
    

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)

