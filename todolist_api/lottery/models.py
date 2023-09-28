from django.db import models
from user.models import MyUser

# Create your models here.
class Card(models.Model):
    RARITY_CHOICES = [
        ("3", "General"),
        ("4", "Rare"),
        ("5", "Epic"),
        ("6", "Legendary"),
    ]

    title = models.CharField(max_length=200, null=False)
    rarity = models.CharField(max_length=1, choices=RARITY_CHOICES)

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CardStock(models.Model):

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) +' '+str(self.card) 
