from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
# Create your views here.


class CreatePersonView(APIView):

    def post(self, request):

        new_person = request.data.get('person')
        serializer = PersonSerializer(data=new_person)

        if serializer.is_valid(raise_exception=True):
            person_created = serializer.save()

        return Response({"success": f'Person with id {person_created.id} added successfully'})
