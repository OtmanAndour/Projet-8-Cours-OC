from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext

def test_i18n(request):
    nb_chats = 1
    couleur = "blanc"
    chaine = _("Bonjour les nouveaux !")
    ip = _("Votre IP est %s") % request.META['REMOTE_ADDR']
    infos = ungettext(
        "… et selon mes informations, vous avez %s chat %s !",
        "… et selon mes informations, vous avez %s chats %ss !",
        nb_chats) % (nb_chats, couleur)

    return render(request, 'i18n/test_i18n.html', locals())