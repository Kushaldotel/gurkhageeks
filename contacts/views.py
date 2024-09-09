from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactFormSerializer

# Create your views here.


class ContactFormView(APIView):
    @swagger_auto_schema(request_body=ContactFormSerializer)
    def post(self, request):
        data = request.data
        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
