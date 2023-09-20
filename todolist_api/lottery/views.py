from django.shortcuts import render

from .models import Card
from .serializers import CardSerializer
import random
from rest_framework.response import Response
from rest_framework.views import APIView 

from .utils import get_random_star
# Create your views here.

class CardView(APIView):
    
    def get(self, request):
        random_star = str(get_random_star())

        cards = Card.objects.filter(rarity=random_star)

        if cards:
            card_index = random.randint(0, len(cards)-1)
            card = cards[card_index]

            serializer = CardSerializer(card)

            return Response({'card': serializer.data})
        
        else:
            return Response({'msg':'no card '+str(random_star)})

    def post(self, request):

        serializer = CardSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error)