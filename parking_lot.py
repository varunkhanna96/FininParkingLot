class Car:
    def __init__(self, reg_no, color):
        self.registration_no = reg_no
        self.color = color

class ParkingArea:
    def __init__(self):
        self.total_slots = None
        self.available_slots = list()

    def create_slots(self, number_of_slots):
        self.total_slots = number_of_slots
        self.available_slots = [i for i in range(1, number_of_slots+1)]