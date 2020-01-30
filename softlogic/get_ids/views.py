from rest_framework.response import Response
from rest_framework.views import APIView
from create_person.models import Person

# Create your views here.


class PesonsIdView(APIView):

    def get(self, request):
        persons = Person.objects.all()
        persons_ids = [x.id for x in persons]
        return Response({"All objects ids": persons_ids})
