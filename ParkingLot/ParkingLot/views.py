from rest_framework.views import APIView
from rest_framework import generics
from .models import ParkingDetails, ParkingLotSlots
from .serializers import (ParkingDetailsSerializer, ParkVehicleSerializer, AddSlotsSerializer,
                          LeaveSlotSerializer)
from rest_framework.response import Response
from .constants import ParkingConst
from django.db import IntegrityError


class AddSlotsView(generics.GenericAPIView):
    serializer_class = AddSlotsSerializer

    def post(self, request):
        serializer = AddSlotsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        number_of_slots = request.data['number_of_slots']
        objs = [ParkingLotSlots() for i in range(0, int(number_of_slots))]
        slots = ParkingLotSlots.objects.bulk_create(objs)
        return Response({'status': 'Successfully created '+str(number_of_slots)+' slots'}, status=200)


class ParkingDetailsView(generics.ListAPIView):
    queryset = ParkingDetails.objects.all()
    serializer_class = ParkingDetailsSerializer


class ParkVehicleView(generics.GenericAPIView):
    serializer_class = ParkVehicleSerializer

    def post(self, request):
        serializer = ParkVehicleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        parking_slot = ParkingLotSlots.objects.filter(status=ParkingConst.FREE.value).first()
        if not parking_slot:
            return Response({'error': 'Parking Lot is full.'},
                            status=417)
        try:
            park = ParkingDetails.objects.create(slot_no=parking_slot,
                                                 car_registration_number=serializer.data['car_registration_number'],
                                                 car_color=serializer.data['car_color'])
            parking_slot.status = ParkingConst.OCCUPIED.value
            parking_slot.save()
        except IntegrityError:
            return Response({'error': 'Car with same registration number has already been parked.'},
                            status=417)
        return Response({'status': 'Successfully Parked on slot '+str(parking_slot.id), 'data': serializer.data}, status=200)


class LeaveSlotView(generics.GenericAPIView):
    serializer_class = LeaveSlotSerializer

    def post(self, request):
        serializer = LeaveSlotSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        try:
            park_slot = ParkingLotSlots.objects.get(id=request.data['slot_no'], status=ParkingConst.OCCUPIED.value)
            park_slot.status = ParkingConst.FREE.value
            park_slot.parkingdetails.delete()
            park_slot.save()
            return Response({'status': 'Slot number {} is free'.format(park_slot.id)}, status=200)
        except ParkingLotSlots.DoesNotExist:
            return Response({'error': 'Parking slot is free or does not exist.'},
                            status=417)


class RegistrationNumberForCarsWithColor(APIView):

    def get(self, request, *args, **kwargs):
        registration_number = ParkingDetails.objects.filter(car_color__iexact=kwargs['color']).\
            values_list('car_registration_number', flat=True)
        if registration_number:
            registration_number = ','.join(registration_number)
        else:
            registration_number = 'Not Found'
        return Response({'registration_number': registration_number}, status=200)


class SlotNumberForCarsWithColor(APIView):

    def get(self, request, *args, **kwargs):
        slot_no = ParkingDetails.objects.filter(car_color__iexact=kwargs['color']).\
            values_list('slot_no', flat=True)
        if slot_no:
            slot_no = ','.join(slot_no)
        else:
            slot_no = 'Not Found'
        return Response({'registration_number': slot_no}, status=200)


class SlotNumberForRegistrationNumber(APIView):

    def get(self, request, *args, **kwargs):
        slot_no = ParkingDetails.objects.filter(car_registration_number__iexact=kwargs['reg_no']).\
            values_list('slot_no', flat=True)
        if slot_no:
            slot_no = ','.join(slot_no)
        else:
            slot_no = 'Not Found'
        return Response({'registration_number': slot_no}, status=200)