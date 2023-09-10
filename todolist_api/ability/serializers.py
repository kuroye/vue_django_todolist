from rest_framework import serializers
from .models import Ability, AbilityGroup

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'


class AbilityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbilityGroup
        fields = '__all__'