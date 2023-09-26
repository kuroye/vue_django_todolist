from rest_framework import serializers
from .models import Card, CardStock

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['rarity'] = obj.get_rarity_display()
        return data

class CardStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardStock
        fields = '__all__'

    def to_representation(self, obj):

        
        data = super().to_representation(obj)

        card_info = Card.objects.filter(id=data['card']).first()
        # print(card_info)
        ser_card_info = CardSerializer(card_info)
        # print(ser_card_info)
        data['card']= ser_card_info.data
        # print(data['card'])
        return data
