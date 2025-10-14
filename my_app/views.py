from django.shortcuts import render
from .models import Card
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/details.html', {'card': card})

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

class CardUpdate(UpdateView):
    model = Card
    fields = ['oracle_text', 'power', 'toughness']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'