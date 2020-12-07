from django.forms import ModelForm
from .models import Player

from django import forms

class NameForm(ModelForm):
  #  your_name = forms.CharField(label='Your name', max_length=100)
  
    class Meta:
       model = Player
       fields = ('name',)

class AdventureForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    answer = forms.CharField(max_length=20)
    room = forms.CharField(max_length=20)
    current_player = forms.CharField(max_length=200)