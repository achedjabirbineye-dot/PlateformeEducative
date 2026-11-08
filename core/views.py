from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from .models import Ressource # <--- On importe le modèle
from django.shortcuts import render, redirect
from .forms import InscriptionForm

def accueil(request):
    lang = request.GET.get('lang', 'fr')
    
    with translation.override(lang):
        message_bienvenue = _("Bienvenue sur notre plateforme éducative !")
        
        # On récupère toutes les ressources de la base de données
        ressources = Ressource.objects.all()
        
        return render(request, 'core/accueil.html', {
            'message': message_bienvenue,
            'ressources': ressources # <--- On les envoie au HTML
        })

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil') # Redirige vers l'accueil après succès
    else:
        form = InscriptionForm()
    
    return render(request, 'core/inscription.html', {'form': form})