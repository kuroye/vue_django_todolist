from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['rarity'] = obj.get_rarity_display()
        return data
