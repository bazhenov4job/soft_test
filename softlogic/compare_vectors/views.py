from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from create_person.models import Person
from django.shortcuts import get_object_or_404
from math import sqrt

# Create your views here.


class CompareVectorsView(APIView):
    parser_classes = [FormParser, ]

    def post(self, request):

        person_1_id = request.query_params.get('person_1')
        person_2_id = request.query_params.get('person_2')
        vector_1 = Person.objects.get(pk=person_1_id).vector
        vector_2 = Person.objects.get(pk=person_2_id).vector
        "Забрать данные из JSON формата поля"
        array_1 = vector_1['vector']
        array_2 = vector_2['vector']
        euclid_distance = sqrt(sum(map(lambda x: (x[0] - x[1]) ** 2, zip(array_1, array_2))))

        return Response({
            'message': f'Euclid Distance between given vectors is {euclid_distance}'
        })
