from django.shortcuts import render
from .serializers import ContactFormSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ContactFormView(APIView):
    def post(self, request):
        data= request.data
        serializer= ContactFormSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

