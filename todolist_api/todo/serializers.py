from dataclasses import fields
import imp
from operator import imod
from pyexpat import model
from re import I
from statistics import mode
from unittest.util import unorderable_list_difference
from rest_framework import serializers
from .models import Todo
from ability.models import Ability
from ability.serializers import AbilitySerializer

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        subject_id = data['subject']
        subject_in_letter = ''
        for i in subject_id:
            ability_data = Ability.objects.filter(pk=i).first()
            serialized_data = AbilitySerializer(ability_data).data
            if(len(subject_id)==1):
                subject_in_letter += serialized_data.get('subject')
            else:
                subject_in_letter += serialized_data.get('subject') + ' '
        
        data['subject'] = {}
        data['subject']['subject_id'] = subject_id
        data['subject']['subject_in_letter'] = subject_in_letter

        return data

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'