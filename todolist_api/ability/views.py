from email.headerregistry import Group
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView 

from .serializers import AbilitySerializer, AbilityGroupSerializer

from .models import Ability, AbilityGroup

# Create your views here.


# 需要返回只属于此用户的Ability
class AbilityView(APIView):
    
    def get(self, request):
        # print("GETTO DAZE")
        id =int( request.GET.get("user_id"))
        
        #一个用户可能有多个group
        groups = AbilityGroup.objects.filter(user=id)
        # abilities = Ability.objects.all()
        # print("I AM GROUPS", groups)

        if groups:
            abilities = []
            #找到属于每一个Group的Ability
            for group in groups:
                # print("I AM GROUP", group)
                filtered_abilities = Ability.objects.filter(group=group.id)
                # print("I AM Filtered ABILITIES", filtered_abilities)
                
                if filtered_abilities:
                    abilities.append(filtered_abilities)

                    # print("I AM ABILITIES", abilities)
            
            serialized_abilities = []    
            
            for ability in abilities:
                serialized_abilities.extend(AbilitySerializer(ability, many=True).data)
            
            # serialized_abilities = AbilitySerializer(abilities, many=True)

            print(serialized_abilities[0])
            return Response({'abilities': serialized_abilities})
        else:
            return Response({'msg': 'No ability lah'})

    def post(self, request):

        serializer = AbilitySerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

        return Response(serializer.errors)  

class AbilityGroupView(generics.ListCreateAPIView):

    queryset = AbilityGroup.objects.all()
    serializer_class = AbilityGroupSerializer


class AbilityGroupWithAbilityView(APIView):

    def get(self, request):
        
        id =int( request.GET.get("user_id"))

        # result list
        ability_group_with_abilities_list = []

        groups = AbilityGroup.objects.filter(user=id)

        if groups is None:
            return Response({'msg':'No Group lah'})
        
        for group in groups:
            abilities = Ability.objects.filter(group=group)
            serialized_abilities = AbilitySerializer(abilities, many=True).data
            
            ability_group_with_abilities_list.append(
                {
                    group.name: serialized_abilities,
                    'group_id': group.id
                }
            )


        return Response(ability_group_with_abilities_list)


class SingleAbilityGroupWithAbilityView(APIView):

    def get(self, request, pk):
        
        
        ability_group_with_abilities_dict = {}

        group = AbilityGroup.objects.filter(pk=pk).first()

        

        abilities = Ability.objects.filter(group=group)

        serialized_abilities = AbilitySerializer(abilities, many=True).data
            
        ability_group_with_abilities_dict[group.name] = serialized_abilities
        ability_group_with_abilities_dict['group_id'] = group.pk
        
        return Response([ability_group_with_abilities_dict])


class UserAbilityUpdateAPIView(APIView):

    def post(self, request):

        user_id = request.data['user_id']
        abilities = request.data['ability']

        print("I AM ABILITIES",abilities)
        for ability_id in abilities: 
            print("I AM ABILITY IN LOOP",ability_id)
            ability = Ability.objects.get(id=ability_id)
            ability.score = ability.score + 1
            a = ability.save()
            print('I AM AAAA', ability.score)
            if a:
                print('ability'+ ability.id +' is saved')

        return Response({'msg': 'ability is ok lah'})