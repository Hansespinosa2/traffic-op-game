from collections import deque
# Intersection base class

class Intersection:
    def __init__(self, x_pos, y_pos, type_):
        self.type_ = type_
        self.x_pos = x_pos
        self.y_pos = y_pos

class Entrance:
    def __init__(self):
        super().__init__(type_="Entrance")

class Exit:
    def __init__(self):
        super().__init__(type_="Exit")


class Roundabout(Intersection):
    def __init__(self):
        super().__init__(type_='Roundabout')
        self.occupied_sections = []  # Tracks occupied sections (degrees)

    def can_enter(self, vehicle_type):
        if vehicle_type == 'Moped':
            free_section = 60
        elif vehicle_type == 'Bus':
            free_section = 120
        else:
            free_section = 90

        occupied_space = sum(section[1] - section[0] for section in self.occupied_sections)
        return occupied_space + free_section <= 360

    def enter(self, vehicle_type):
        if self.can_enter(vehicle_type):
            if vehicle_type == 'Moped':
                section = (0, 60)
            elif vehicle_type == 'Bus':
                section = (0, 120)
            else:
                section = (0, 90)
            self.occupied_sections.append(section)

class StopSign(Intersection):
    def __init__(self):
        super().__init__(type_='StopSign')
        self.queue = deque()

    def add_to_queue(self, vehicle):
        self.queue.append(vehicle)

    def process_queue(self):
        if self.queue:
            return self.queue.popleft()

class TrafficLight(Intersection):
    def __init__(self, mode, param):
        super().__init__(type_='TrafficLight')
        self.mode = mode
        self.param = param
        self.time_elapsed = 0
        self.car_queue = deque()
        self.light_state = 'Red'

    def update_light(self):
        if self.mode == 'Timer':
            if self.time_elapsed >= self.param:
                self.light_state = 'Green' if self.light_state == 'Red' else 'Red'
                self.time_elapsed = 0
        elif self.mode == 'Sensor':
            if len(self.car_queue) > self.param:
                self.light_state = 'Green'
            else:
                self.light_state = 'Red'
        elif self.mode == 'Sensor-Timer':
            if len(self.car_queue) > self.param or self.time_elapsed >= self.param:
                self.light_state = 'Green'
                self.time_elapsed = 0
            else:
                self.light_state = 'Red'

    def add_to_queue(self, vehicle):
        self.car_queue.append(vehicle)