from django.db import models

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

    def __str__(self):
        return self.title