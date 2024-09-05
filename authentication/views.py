# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, ProfileSerializer, TermsandServicesSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.parsers import MultiPartParser
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import TermsandServices
from drf_yasg.utils import swagger_auto_schema
User=get_user_model()


class RegisterView(ModelViewSet):
    parser_classes=[MultiPartParser]
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer
    )
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token_generator=default_token_generator
            uid= urlsafe_base64_encode(force_bytes(user.pk))
            token= token_generator.make_token(user)

            if settings.DEBUG:
                conformation_link= f"http://localhost:5173/auth/confirm/{uid}/{token}/"
            else:
                conformation_link=f"https://gorkhageeks-backend.onrender.com/auth/confirm/{uid}/{token}/"

                conformation_link=f"https://gurkhageeks-frontend.vercel.app/auth/confirm/{uid}/{token}/"

            subject= "Confirm your registration"
            html_message= render_to_string("blog/confirmation_email.html",{'confirmation_link':conformation_link})
            plain_message= strip_tags(html_message)
            from_email= settings.EMAIL_HOST_USER
            to_email= user.email
            try:
                send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
                response_data = {
                "message": "Registration email sent for confirmation"
                    }
                return Response({'status': response_data}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([AllowAny])
def confirm_registration(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.user_type = 'developer'
            user.save()
            return Response({"message": "Registration successful"})
        else:
            return Response({"message": "Invalid token"})
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response(status=="Invalid user")

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
class LoginView(APIView):
    @swagger_auto_schema(
        operation_description="User login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),)
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_joined": user.date_joined,
                "is_active": user.is_active,
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    @swagger_auto_schema(operation_description="User logout",
                         request_body=openapi.Schema(
                             type= openapi.TYPE_OBJECT,
                             properties={
                                 'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh token'),
                             }
                         )
                         )
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("message:logged out",status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response(
                {"error": "Refresh token not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception:
            return Response(
                {"error": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
class ProfileView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self,request):
        serializer= ProfileSerializer(request.user)
        return Response(serializer.data)

class TermsandServicesView(ListAPIView):
    queryset= TermsandServices.objects.all()
    serializer_class= TermsandServicesSerializer