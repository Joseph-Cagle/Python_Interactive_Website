from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .forms import NameForm, AdventureForm
from .models import Player
from pytz import timezone


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
    context = {}
    
    if request.method == "POST":
        form = AdventureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            current_location = data.get("location")
            answer = data.get("answer")

        


  
def adventureRight(request):

    return render(request, 'playerChoosesRight.html')
    
