from django.db import models
from django.urls import reverse

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    oracle_text = models.CharField(max_length=250)
    power = models.IntegerField()
    toughness = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("card-detail", kwargs={"card_id": self.id})

class Comment(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=250)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f'created on {self.time_stamp}'
    
class Collection(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("collection-detail", kwargs={"pk": self.id})
    