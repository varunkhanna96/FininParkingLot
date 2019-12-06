from rest_framework import serializers
from .models import ParkingDetails


class ParkingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingDetails
        fields = '__all__'


class AddSlotsSerializer(serializers.Serializer):
    number_of_slots = serializers.IntegerField(max_value=20)


class ParkVehicleSerializer(serializers.Serializer):
    car_registration_number = serializers.CharField(max_length=40)
    car_color = serializers.CharField(max_length=10)


class LeaveSlotSerializer(serializers.Serializer):
    slot_no = serializers.IntegerField()

class ResponseSerializer(serializers.Serializer):
    registration_numbers = serializers.CharField()