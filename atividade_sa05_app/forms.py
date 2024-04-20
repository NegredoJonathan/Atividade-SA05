from django import forms
from atividade_sa05_app.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'nascimento', 'email', 'countryToWork']
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'nascimento': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'countryToWork': forms.TextInput(attrs={ 'class': 'form-control' }),   
        }