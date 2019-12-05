from django.core.management.base import BaseCommand, CommandError
from ParkingLot.ParkingLot.parking_lot import Car, ParkingArea


parking_lot = ParkingArea()


class Command(BaseCommand):
    def handle(self, *args, **options):
        return
