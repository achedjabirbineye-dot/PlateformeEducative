from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from .models import Ressource # <--- On importe le modèle
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RessourceForm

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

    # Cette petite fonction vérifie si l'utilisateur est un prof
def est_professeur(user):
    return user.is_authenticated and user.role == 'prof'

# @login_required : oblige à être connecté
# @user_passes_test : oblige à être un prof, sinon renvoie vers l'accueil
@login_required
@user_passes_test(est_professeur, login_url='/')
def ajouter_ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accueil') # Redirige vers l'accueil après l'ajout
    else:
        form = RessourceForm()
    
    return render(request, 'core/ajouter_ressource.html', {'form': form})