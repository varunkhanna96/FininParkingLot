from rest_framework import serializers
from .models import ParkingDetails


class ParkingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingDetails
        fields = '__all__'


class AddSlotsSerializer(serializers.Serializer):
    number_of_slots = serializers.IntegerField()


class ParkVehicleSerializer(serializers.Serializer):
    car_registration_number = serializers.CharField(max_length=40)
    car_color = serializers.CharField(max_length=10)