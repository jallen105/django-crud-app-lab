from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cards/', views.cards_index, name='card-index'),
    path('cards/<int:card_id>/', views.card_detail, name='card-detail'),
    path('cards/create/', views.CardCreate.as_view(), name='card-create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),
    path('cards/<int:card_id>/add-comment', views.add_comment, name='add-comment'),
    path('collections/', views.CollectionList.as_view(), name='collection-index'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collection-create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collection-update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collection-delete'),
    path('collections/<int:collection_id>/add-card/<int:card_id>/', views.add_card, name='add-card'),
    path('collections/<int:collection_id>/remove-card/<int:card_id>/', views.remove_card, name='remove-card'),
    path('accounts/signup/', views.signup, name='signup'),
]
