from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=200)
   
    

    def gameover(self):
        self.game_end = timezone.now()
        self.save()

    def __str__(self):
        return self.name
   

#class theAdventure(models.Model):
 #    name = models.CharField(max_length=200)
  #   answer = models.CharField(max_length=20)
   #  direction = models.CharField(max_length=20)

#class AdventureForm(forms.Form):
     #answer = forms.CharField(max_length=20)
    # direction = forms.CharField(max_length=20)
  
