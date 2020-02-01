from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from create_person.models import Person
from create_person.serializers import PersonSerializer
from django.shortcuts import get_object_or_404
import numpy as np
from PIL import Image

# Create your views here.


class AddVectorView(APIView):
    parser_classes = [MultiPartParser, ]


    def post(self, request, **kwargs):
        size = (300, 300)
        pk = kwargs.get('pk')
        person = get_object_or_404(Person, pk=pk)
        # print(request.data)
        file_obj = request.FILES['image']
        new_image = Image.open(file_obj.name)
        new_image.load()
        new_image.thumbnail(size)
        arr = np.asanyarray(new_image, dtype='uint8')
        arr = np.ravel(arr)
        arr = list(arr)
        arr = map(int, arr)
        arr = map(lambda x: x / 255.0, arr)
        json_arr = {"vector": list(arr)}
        person.vector = json_arr
        person.save()
        return Response({
            "success": f"Person with id={pk} now has vector performance"
        })
