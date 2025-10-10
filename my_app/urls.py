from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('cards/', views.cards_index, name='cards-index'),
]
