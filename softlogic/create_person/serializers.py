from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=64)
    second_name = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)
