from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from create_person.models import Person
import numpy as np
from PIL import Image

# Create your views here.


class AddVectorView(APIView):
    parser_classes = [FileUploadParser,]

    def get(self, request):
        return self.put(request)

    def put(self, request):
        file_obj = request.FILES['file']
        new_image = Image.open(file_obj)
        new_image.load()
        arr = np.asanyarray(new_image, dtype='uint8')
        arr = np.ravel(arr)
        return Response({"array is": arr[:10]})
