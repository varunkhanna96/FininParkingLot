from rest_framework.views import APIView
from rest_framework import generics
from .models import ParkingDetails, ParkingLotSlots
from .serializers import ParkingDetailsSerializer, ParkVehicleSerializer, AddSlotsSerializer
from rest_framework.response import Response
from .constants import ParkingConst
from django.db import IntegrityError


class AddSlotsView(APIView):
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


class ParkVehicleView(APIView):

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
        except IntegrityError:
            return Response({'error': 'Car with same registration number has already been parked.'},
                            status=417)
        return Response({'status': 'Successfully Parked', 'data': serializer.data}, status=200)