from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
def homePage(request):
    form = NameForm()
    context = {'form':form}
    return render(request, 'home.html', context)