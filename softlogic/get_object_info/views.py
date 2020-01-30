from django.shortcuts import render
from create_person.serializers import PersonSerializer
from rest_framework.views import APIView
# Create your views here.


class ReturnInfoView(APIView):

    def post(self, request):
        person

