import random
# Extra factors
class PedestrianCrosswalk:
    def __init__(self):
        self.blocked = random.choice([True, False])

    def is_blocked(self):
        return self.blocked

class ParkingLot:
    def __init__(self):
        pass

    def car_parks(self):
        return random.random() < 0.05