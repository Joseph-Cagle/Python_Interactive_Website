from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
from .models import Player
from pytz import timezone

# Create your views here.
def homePage(request):
    form = NameForm()
    context = {'form':form}
    return render(request, 'home.html', context)

def index(request):
    players = Player.objects.filter(game_end__lte=timezone.now()).order_by("game_end")
    return render(request, 'myfirstgame/index.html', {'players':players})