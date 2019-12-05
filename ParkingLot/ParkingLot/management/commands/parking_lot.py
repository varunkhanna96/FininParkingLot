from collections import OrderedDict, defaultdict


class Car:
    def __init__(self, reg_no, color):
        self.registration_no = reg_no
        self.color = color


class ParkingArea:
    def __init__(self):
        self.total_slots = None
        self.available_slots = list()
        self.slot_car_map = OrderedDict()
        self.reg_no_slot_map = dict()
        self.color_reg_map = defaultdict(list)

    def create_slots(self, number_of_slots):
        self.total_slots = number_of_slots
        self.available_slots = [i for i in range(1, number_of_slots+1)]
        print('Created a parking lot with {} slots'.format(number_of_slots))
        return True

    def park(self, number, color):
        if self.available_slots:
            car = Car(number, color)
            slot = self.available_slots.pop()
            self.slot_car_map[slot] = car
            self.reg_no_slot_map[number] = slot
            self.color_reg_map[color].append(number)
            print('Car parked on slot number {}'.format(slot))
            return slot
        else:
            print('Parking Lot is full. Please come back later.')

    def leave(self, slot):
        if slot in self.available_slots:
            print('There is no car parked in the given slot.')
            return False
        self.available_slots.append(slot)
        car = self.slot_car_map[slot]
        del self.slot_car_map[slot]
        del self.reg_no_slot_map[car.registration_no]
        self.color_reg_map[car.color].remove(car.registration_no)
        print('Slot number {} is free'.format(slot))
        return True

    def status(self):
        print("Slot No.  Registration No  Colour")
        for slot, car in self.slot_car_map.items():
            print("{}         {}    {}".format(slot, car.registration_no, car.color))
        return True

    def slot_number_for_registration_number(self, reg_no):
        slot_number = None
        if reg_no in self.reg_no_slot_map:
            slot_number = self.reg_no_slot_map[reg_no]
            print(slot_number)
            return slot_number
        else:
            print("Not found")
            return slot_number

    def registration_numbers_for_cars_with_colour(self, color):
        reg_number = self.color_reg_map[color]
        print(", ".join(reg_number))
        return self.color_reg_map[color]

    def slot_numbers_for_cars_with_colour(self, color):
        reg_numbers = self.color_reg_map[color]
        slots = [self.reg_no_slot_map[reg_number] for reg_number in reg_numbers]
        print(", ".join(map(str, slots)))
        return slots
