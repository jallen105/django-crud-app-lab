from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def details(request):
    return HttpResponse('details page')

def cards_index(request):
    return HttpResponse('Cards index page')