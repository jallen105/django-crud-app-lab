from django.shortcuts import render, redirect
from .models import Card, Collection, CardCollection
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('card-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class Home(LoginView):
    template_name = 'home.html'

@login_required
def card_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    comment_form = CommentForm()
    return render(request, 'cards/details.html', {'card': card, 'comment_form': comment_form})

@login_required
def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = '__all__'

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['oracle_text', 'power', 'toughness']

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

@login_required
def add_comment(request, card_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.card_id = card_id
        new_comment.save()
    return redirect('card-detail', card_id=card_id)

class CollectionCreate(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CollectionUpdate(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ['name']

class CollectionList(LoginRequiredMixin, ListView):
    model = Collection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_collection'] = Collection.objects.filter(user = self.request.user)
        return context

class CollectionDetail(LoginRequiredMixin, DetailView):
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionDetail, self).get_context_data(**kwargs)
        context['card_list'] = Card.objects.all()
        context['card_collection'] = CardCollection.objects.filter(collection_id=self.kwargs['pk'])
        return context

class CollectionDelete(LoginRequiredMixin, DeleteView):
    model = Collection
    success_url = '/collections/'

@login_required
def add_card(request, collection_id, card_id):
    card_collection_queryset = CardCollection.objects.filter(collection_id=collection_id, card_id=card_id)
    if card_collection_queryset.exists():
        add_card = CardCollection.objects.get(collection_id=collection_id, card_id=card_id)
        add_card.quantity+=1
        add_card.save()
    else:
        Collection.objects.get(id=collection_id).cards.add(card_id)
    return redirect('collection-detail', pk=collection_id)

@login_required
def remove_card(request, card_id, collection_id):
    card_collection_queryset = CardCollection.objects.get(collection_id=collection_id, card_id=card_id)
    if card_collection_queryset.quantity > 1:
        add_card = CardCollection.objects.get(collection_id=collection_id, card_id=card_id)
        add_card.quantity-=1
        add_card.save()
    else:
        Collection.objects.get(id=collection_id).cards.remove(card_id)
    return redirect('collection-detail', pk=collection_id)