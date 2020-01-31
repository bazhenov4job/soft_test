from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from create_person.models import Person
from create_person.serializers import PersonSerializer
from django.shortcuts import get_object_or_404
import numpy as np
from PIL import Image

# Create your views here.


class AddVectorView(APIView):
    parser_classes = [FileUploadParser,]

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        person = get_object_or_404(Person, pk=pk)
        new_image = Image.open('granny_pain.jpg')
        new_image.load()
        arr = np.asanyarray(new_image, dtype='uint8')
        arr = np.ravel(arr)
        image_dict = {'vector': arr}
        serializer = PersonSerializer(instance=person, data=image_dict)
        if serializer.is_valid(raise_exception=True):
            person_saved = person.save()

        return Response ({
            "success": f"Person with id={pk} now has vetor performanse"
        })

    # def put(self, request):
    #     file_obj = request.FILES['file']
    #     new_image = Image.open(file_obj)
    #     new_image.load()
    #     arr = np.asanyarray(new_image, dtype='uint8')
    #     arr = np.ravel(arr)
    #     return Response({"array is": arr[:10]})
