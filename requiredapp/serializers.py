from rest_framework.serializers import ModelSerializer
from .models import TalimShakli, Nation, Sex, Region, District, PassportFuqaroligi

class TalimShakliSerializer(ModelSerializer):
    class Meta:
        model = TalimShakli
        fields = "__all__"

class NationSerializer(ModelSerializer):
    class Meta:
        model = Nation
        fields = "__all__"

class SexSerializer(ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"

class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"

class PassportFuqaroligiSerializer(ModelSerializer):
    class Meta:
        model = PassportFuqaroligi
        fields = "__all__"