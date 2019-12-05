class Car:
    def __init__(self, reg_no, color):
        self.registration_no = reg_no
        self.color = color


class ParkingArea:
    def __init__(self):
        self.total_slots = None
        self.available_slots = list()
        self.slot_car_map = dict()

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
            return slot
        else:
            print('Parking Lot is full. Please come back later.')

    def leave(self, slot):
        if slot in self.available_slots:
            print('There is no car parked in the given slot.')
            return False
        self.available_slots.append(slot)
        del self.slot_car_map[slot]
        print('Slot number {} is free'.format(slot))
        return True

    def status(self):
        print("Slot No.  Registration No  Colour")
        for slot, car in self.slot_car_map.items():
            print("{}         {}    {}".format(slot, car.registration_no, car.color))
        return True
