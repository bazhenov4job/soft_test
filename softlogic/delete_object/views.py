from django.shortcuts import render
from rest_framework.response import Response
from create_person.models import Person
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.


class DeleteObjectView(APIView):

    def delete_obj(self, person_id):

        person = get_object_or_404(Person, pk=person_id)
        person.delete()
        return Response({
            "message": f"Object with id = {person_id} deleted",
        }, status=204)

    def get(self, request, **kwargs):

        person_id = kwargs.get('pk')

        return self.delete_obj(person_id)
