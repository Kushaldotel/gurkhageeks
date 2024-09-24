from django.shortcuts import render
from rest_framework import generics
from .serializers import GoogleLoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class GoogleLoginApiView(generics.GenericAPIView):
    serializer_class= GoogleLoginSerializer

    def post(self, request):
        token= self.request.data('token')
        serializer= self.get_serializer(data= request.data)
        if serializer.is_valid(raise_exception= True):
            token= serializer.validated_data['token']
            response= request.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={token}')
            
            if response.status_code != 200:
                return Response({'message': 'Invalid token'}, status= 400)
            
            user_info= response.json()
            email= user_info.get("email")

            user, create= user.objects.get_or_create(email= email)

            refresh= RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })