from django.shortcuts import render

def test_i18n(request):
    nb_chats = 1
    couleur = "blanc"
    chaine = "Bonjour les nouveaux !"
    ip = "Votre IP est %s" % request.META['REMOTE_ADDR']
    infos = "… et selon mes informations, vous avez %s chats %s !" % (nb_chats, couleur)

    return render(request, 'i18n/test_i18n.html', locals())
