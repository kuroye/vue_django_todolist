from django.shortcuts import render

from .models import Card, CardStock
from .serializers import CardSerializer, CardStockSerializer
import random
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics 

from .utils import get_random_star
# Create your views here.

# All card of that user
class AllCardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request):
        print(request.GET.get("id"))
        id =int(request.GET.get("id") )
        # print("I AM USER ID ", id)
        card_data = Card.objects.filter(user=id)
        # todo_data = self.get_queryset()
        ser = CardSerializer(card_data, many=True)
        return Response(ser.data)

# Draw one Card
class CardView(APIView):
    
    def get(self, request):
        random_star = str(get_random_star())

        id =int(request.GET.get("id") )
        cards = Card.objects.filter(user=id).filter(rarity=random_star)

        if cards:
            card_index = random.randint(0, len(cards)-1)
            card = cards[card_index]

            serializer = CardSerializer(card)

            CardStock.objects.create(card=card, user=card.user)

            return Response({'card': serializer.data})
        
        else:
            return Response({'msg':'no card '+str(random_star)})

    # def post(self, request):

    #     serializer = CardSerializer(request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        
    #     return Response(serializer.error)


# Card that user got
class CardStockView(generics.ListCreateAPIView):
    queryset = CardStock.objects.all()
    serializer_class = CardStockSerializer

    def get(self, request):
        print(request.GET.get("id"))
        id =int(request.GET.get("id") )
        # print("I AM USER ID ", id)
        card_stock_data = CardStock.objects.filter(user=id)
        ser = CardStockSerializer(card_stock_data, many=True)
        return Response(ser.data)