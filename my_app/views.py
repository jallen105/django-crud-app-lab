from django.http import HttpResponse
from django.shortcuts import render

class Card:
    def __init__(self, name, oracle_text, power, toughness):
        self.name = name
        self.oracle_text = oracle_text
        self.power = power
        self.toughness = toughness

cards = [
    Card('Llanwar Elf', 'tap add one mana', 1, 1),
    Card('Ghalta', 'Trample', 12, 12),
    Card('Monastery Swiftspear', 'Haste, Prowess', 1, 2),
    Card('Avacyn, Angel of Hope', 'Flying, vigilance, indestructible', 8, 8)
]

def home(request):
    return render(request, 'home.html')

def details(request):
    return HttpResponse('details page')

def cards_index(request):
    return render(request, 'cards/index.html', {'cards': cards})