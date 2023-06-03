from rest_framework.serializers import ModelSerializer
from .models import Passport, Diplom, Contact

class PassportSerializer(ModelSerializer):
    class Meta:
        model = Passport
        fields = "__all__"

class DiplomSerializer(ModelSerializer):
    class Meta:
        model = Diplom
        fields = "__all__"

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

