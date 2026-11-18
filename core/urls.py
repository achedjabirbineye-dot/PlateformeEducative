from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('ajouter/', views.ajouter_ressource, name='ajouter_ressource'),
    path('mes-ressources/', views.mes_ressources, name='mes_ressources'),
    path('modifier/<int:ressource_id>/', views.modifier_ressource, name='modifier_ressource'),
    path('supprimer/<int:ressource_id>/', views.supprimer_ressource, name='supprimer_ressource'),
]