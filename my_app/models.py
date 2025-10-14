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
    