from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import UserProfileSerializer, UserUpdateSerailizer

User = get_user_model()
# Create your views here.


class UserProfileView(ModelViewSet):
    parser_classes = [MultiPartParser]
    http_method_names = ["get", "patch"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter queryset to only include the currently authenticated user
        user_id = self.request.user.id
        return User.objects.filter(id=user_id)

    def get_serializer_class(self):
        # Return different serializers based on HTTP method
        if self.request.method == "GET":
            return UserProfileSerializer
        return UserUpdateSerailizer

    def update(self, request, *args, **kwargs):

        user = self.request.user

        serializer = UserUpdateSerailizer(
            instance=user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
