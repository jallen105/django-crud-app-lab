from django.shortcuts import render, redirect
from .models import Card, Collection
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


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

class CollectionCreate(CreateView):
    model = Collection
    fields = ['name']

class CollectionUpdate(UpdateView):
    model = Collection
    fields = ['name']

class CollectionList(ListView):
    model = Collection

class CollectionDetail(DetailView):
    model = Collection

class CollectionDelete(DeleteView):
    model = Collection
    success_url = '/collections/'