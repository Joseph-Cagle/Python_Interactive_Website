from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .forms import NameForm
from .models import Player
from pytz import timezone


# Create your views here.
def homePage(request):
    return render(request, 'home.html')

#def index(request):
 #   players = Player.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
  #  return render(request, 'myfirstgame/index.html', {'players':players})

def character_page(request):
    thePlayer = Player()
    if request.method =='POST':
        thePlayer.name=request.POST.get("name")
        #thePlayer = Player('',request.POST.get("name")) # '' acounts for autonumber primary key
        return render(request, 'adventure.html', {'thePlayer' : thePlayer})
        #we need to migrate to this is at 1 hour 11 minutes in
    else:
       return render(request, 'character.html')  

def adventurePage(request):
    
    #code to add here

    return render(request, "adventure.html")
    
