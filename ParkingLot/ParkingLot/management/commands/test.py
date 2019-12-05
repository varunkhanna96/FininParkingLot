from .parking_lot import ParkingArea
from django.core.management.base import BaseCommand, CommandError


parking_lot = ParkingArea()
cars = [
    dict(reg_no='KA-01-HH-1234', color='White'),
    dict(reg_no='KA-01-HH-9999', color='White'),
    dict(reg_no='KA-01-HH-7777', color='Black'),
    dict(reg_no='KA-01-HH-1234', color='Red'),
    dict(reg_no='KA-01-HH-2701', color='Blue'),
    dict(reg_no='KA-01-HH-3141', color='Black'),
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        assert parking_lot.create_slots(6) is True

        for i in range(0, len(cars)):
            assert parking_lot.park(cars[i]['reg_no'], cars[i]['color']) == len(cars) - i

        assert parking_lot.leave(4) is True
        assert parking_lot.status() is True

        assert len(parking_lot.available_slots) == 1
        assert parking_lot.park('KA-01-P-333', 'White') == 4

        assert parking_lot.registration_numbers_for_cars_with_colour('White') == ['KA-01-HH-1234',
                                                                                  'KA-01-HH-9999',
                                                                                  'KA-01-P-333']
        assert parking_lot.slot_numbers_for_cars_with_colour('White') == [3, 5, 4]
        assert parking_lot.slot_number_for_registration_number('KA-01-HH-3141') == 1
        assert parking_lot.slot_number_for_registration_number('MH-04-AY-1111') is None
