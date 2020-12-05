from django.forms import ModelForm
from .models import Player

class NameForm(ModelForm):
  #  your_name = forms.CharField(label='Your name', max_length=100)
  class Meta:
      model = Player
      fields = '__all__'