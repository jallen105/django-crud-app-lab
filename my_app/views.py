from django.shortcuts import render, redirect
from .models import Card
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')

def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    comment_form = CommentForm()
    return render(request, 'cards/details.html', {'card': card, 'comment_form': comment_form})

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

def add_comment(request, card_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.card_id = card_id
        new_comment.save()
    return redirect('card-detail', card_id=card_id)