from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from .models import Ressource, Matiere, Favori # <--- On importe le modèle
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RessourceForm
from django.shortcuts import get_object_or_404 

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
            ressource = form.save(commit=False)  # On ne sauvegarde pas encore pour ajouter l'auteur
            ressource.auteur = request.user  # On assigne l'auteur
            ressource.save()  # On sauvegarde finalement
            return redirect('accueil') # Redirige vers l'accueil après l'ajout
    else:
        form = RessourceForm()
    
    return render(request, 'core/ajouter_ressource.html', {'form': form})

@login_required
@user_passes_test(est_professeur, login_url='/')
def mes_ressources(request):
    # On filtre pour n'afficher que les ressources de ce prof précis
    ressources = Ressource.objects.filter(auteur=request.user).order_by('-date_ajout')
    return render(request, 'core/mes_ressources.html', {'ressources': ressources})


@login_required
@user_passes_test(est_professeur, login_url='/')
def supprimer_ressource(request, ressource_id):
    # On récupère la ressource, ou on affiche une erreur 404 si elle n'existe pas
    ressource = get_object_or_404(Ressource, id=ressource_id)
    
    # Sécurité : on vérifie que c'est bien le prof connecté qui a créé cette ressource
    if ressource.auteur == request.user:
        ressource.delete()
        
    return redirect('mes_ressources')

@login_required
@user_passes_test(est_professeur, login_url='/')
def modifier_ressource(request, ressource_id):
    ressource = get_object_or_404(Ressource, id=ressource_id)
    
    # Sécurité : seul l'auteur peut modifier
    if ressource.auteur != request.user:
        return redirect('mes_ressources')
        
    if request.method == 'POST':
        form = RessourceForm(request.POST, request.FILES, instance=ressource)
        if form.is_valid():
            form.save()
            return redirect('mes_ressources')
    else:
        form = RessourceForm(instance=ressource) # On pré-remplit le formulaire avec les données existantes
        
    return render(request, 'core/modifier_ressource.html', {'form': form, 'ressource': ressource})

@login_required
def ajouter_favori(request, ressource_id):
    ressource = get_object_or_404(Ressource, id=ressource_id)
    Favori.objects.get_or_create(utilisateur=request.user, ressource=ressource)
    return redirect(request.META.get('HTTP_REFERER', 'accueil'))

@login_required
def mes_favoris(request):
    favoris = Favori.objects.filter(utilisateur=request.user).order_by('-date_ajout')
    return render(request, 'core/mes_favoris.html', {'favoris': favoris})