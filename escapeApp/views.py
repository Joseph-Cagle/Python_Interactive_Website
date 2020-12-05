from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    html = "<h1>Welcome Vault Dweller, what is your name?</h1>"
    return HttpResponse(html)