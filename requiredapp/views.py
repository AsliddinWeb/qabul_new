from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TalimShakli, Nation, Sex, District, Region, PassportFuqaroligi

from .serializers import TalimShakliSerializer, NationSerializer, \
    SexSerializer, DistrictSerializer, RegionSerializer, PassportFuqaroligiSerializer

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class TalimShakliAW(APIView):
    @swagger_auto_schema(
        operation_description="1. Eng boshlang'ich qism. Ta'lim shakllarini tanlash uchun GET Api!",
        responses={200: TalimShakliSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = TalimShakli.objects.all()
        serializer = TalimShakliSerializer(queryset, many=True)

        return Response(serializer.data)

class NationAW(APIView):
    @swagger_auto_schema(
        operation_description="Millatlar! Passport ma'lumotlarini to'ldirish uchun.",
        responses={200: NationSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = Nation.objects.all()
        serializer = NationSerializer(queryset, many=True)

        return Response(serializer.data)

class SexAW(APIView):
    @swagger_auto_schema(
        operation_description="Jinslar! Passport ma'lumotlarini to'ldirish uchun.",
        responses={200: SexSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = Sex.objects.all()
        serializer = SexSerializer(queryset, many=True)

        return Response(serializer.data)

class DistrictAW(APIView):
    @swagger_auto_schema(
        operation_description="Viloyatlar! Passport ma'lumotlarini to'ldirish uchun.",
        responses={200: DistrictSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = District.objects.all()
        serializer = DistrictSerializer(queryset, many=True)

        return Response(serializer.data)

class RegionAW(APIView):
    @swagger_auto_schema(
        operation_description="Tumanlar! Passport ma'lumotlarini to'ldirish uchun.",
        responses={200: RegionSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = Region.objects.all()
        serializer = RegionSerializer(queryset, many=True)

        return Response(serializer.data)

class PassportFuqaroligiAW(APIView):
    @swagger_auto_schema(
        operation_description="Davlatlar! Passport ma'lumotlarini to'ldirish uchun.",
        responses={200: PassportFuqaroligiSerializer()},
        tags=["INFO API lar"],
    )
    def get(self, request):
        queryset = PassportFuqaroligi.objects.all()
        serializer = PassportFuqaroligiSerializer(queryset, many=True)

        return Response(serializer.data)