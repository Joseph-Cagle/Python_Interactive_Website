from django.forms import ModelForm
from .models import Player

from django import forms

class NameForm(ModelForm):
  
  
    class Meta:
       model = Player
       fields = ('name',)

class AdventureForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    answer = forms.CharField(max_length=20)
    direction = forms.CharField(max_length=20)
    location = forms.CharField(max_length=20)