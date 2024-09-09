from rest_framework.serializers import ModelSerializer

from .models import ContactsForm


class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactsForm
        fields = "__all__"
