# serializers.py
from pydantic import validate_email
from rest_framework import serializers
from .models import CustomUser, TermsandServices, Organisation
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

User=get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name', 'profile_pic', 'bio', 'website']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            profile_pic=validated_data.get('profile_pic', None),
            bio=validated_data.get('bio', ''),
            website=validated_data.get('website', '')
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name', 'last_name', 'profile_pic', 'bio', 'website']

class TermsandServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsandServices
        fields = ['terms',]

class ForgotPasswordSerializer(serializers.Serializer):
    email= serializers.EmailField()
    # class Meta:
    #     model = User
    #     fields = ['email']

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        uid = self.context.get('uidb64')
        token = self.context.get('token')
        new_password = data.get('new_password')

        # Validate user and token
        try:
            # Decode the uidb64 to get the user
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("Invalid user.")

        # Check if the token is valid
        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError("Invalid or expired token.")

        # Validate the new password length
        if len(new_password) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")

        # Store the user in context for use in save method
        self.context['user'] = user

        return data

    def save(self, **kwargs):
        # Get the user from context and set the new password
        uid= self.context.get("uidb64")
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
        new_password = self.validated_data.get('new_password')

        user.set_password(new_password)
        user.save()

        return user

class OrganisationRegistrationSerializer(serializers.ModelSerializer):
    # Defining fields from the Organisation model
    organisation_name = serializers.CharField(max_length=100)
    website = serializers.URLField(max_length=200)
    phone_number = serializers.CharField(max_length=20)
    address = serializers.CharField()
    logo = serializers.ImageField(required=False)
    description = serializers.CharField()

    class Meta:
        model = CustomUser  # This should remain the CustomUser model
        fields = ['email', 'password', 'organisation_name', 'website', 'phone_number', 'address', 'logo', 'description']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Extract organisation-specific fields
        organisation_name = validated_data.pop('organisation_name')
        website = validated_data.pop('website')
        phone_number = validated_data.pop('phone_number')
        address = validated_data.pop('address')
        logo = validated_data.pop('logo', None)
        description = validated_data.pop('description')

        # Create the user (CustomUser model)
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type='organization',
            is_active=False  # Organization users are inactive by default
        )

        # Create the organisation (Organisation model)
        Organisation.objects.create(
            user=user,
            organisation_name=organisation_name,
            website=website,
            email=validated_data['email'],  # Organization email is the same as the user email
            phone_number=phone_number,
            address=address,
            logo=logo,
            description=description
        )

        return user
