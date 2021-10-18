from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from .forms import NameForm, AdventureForm
from .models import Player
from pytz import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def homePage(request):
    return render(request, 'home.html')

#def index(request):
 #   players = Player.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
  #  return render(request, 'myfirstgame/index.html', {'players':players})

def character_page(request):
    context = {}
    current_player = None
   # thePlayer = Player()
    if request.method =='POST':
      form = NameForm(request.POST)
      if form.is_valid():
        player = form.save()
        player.save()
        context['current_player'] = player.name
        return render(request, 'adventure.html', context)
    else:
        form = NameForm()
    context['form'] = form

    return render(request, 'character.html')   

def adventurePage(request):
    
    return render(request, 'adventure.html')
        
def adventureRight(request):

    return render(request, 'playerChoosesRight.html')

def adventureLeft(request):

    return render(request, 'playerChoosesleft.html')

def adventureStraight(request):

    return render(request, 'playerChoosesStraight.html')   

def backToVault(request):

    return render(request, 'backToVault.html')

def register(response):
    if response.method =="POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("http://127.0.0.1:8000")
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    return render(response,"register.html", {"form":form})


    
