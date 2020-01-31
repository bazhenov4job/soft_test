from django.shortcuts import render
from create_person.serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from create_person.models import Person
from django.shortcuts import get_object_or_404
# Create your views here.


class ReturnInfoView(APIView):

    def get(self, request, **kwargs):

        person_id = kwargs.get('pk')
        person = get_object_or_404(Person, pk=person_id)
        first_name = person.first_name
        second_name = person.second_name
        vector = True if person.vector else False
        return Response({
            "first_name": first_name,
            "second_name": second_name,
            "vector": vector,
        })
