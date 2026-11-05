from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation

def accueil(request):
    # On récupère la langue (français par défaut)
    lang = request.GET.get('lang', 'fr')
    
    # On force la traduction pour cette page
    with translation.override(lang):
        message_bienvenue = _("Bienvenue sur notre plateforme éducative !")
        return render(request, 'core/accueil.html', {'message': message_bienvenue})