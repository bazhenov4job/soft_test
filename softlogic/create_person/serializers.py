from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=64)
    second_name = serializers.CharField(max_length=128)
    vector = serializers.JSONField(required=False)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.second_name = validated_data.get('second_name', instance.second_name)
        instance.vector = validated_data.get('vector', instance.vector)

        instance.save()
        return instance
