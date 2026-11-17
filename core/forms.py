from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Ressource 
class InscriptionForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'serie', 'langue']
        
    # On personnalise un peu l'apparence des champs (optionnel, mais plus joli)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RessourceForm(forms.ModelForm):
    class Meta:
        model = Ressource
        fields = ['titre', 'fichier', 'matiere', 'type_ressource', 'langue']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'