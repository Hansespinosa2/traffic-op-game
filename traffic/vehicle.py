# Base Vehicle class
from road import Road
class Vehicle:
    def __init__(self, max_speed, entrance, exit, paths):
        self.max_speed = max_speed
        self.entrance = entrance
        self.exit = exit
        self.paths = [road for road in paths if isinstance(road, Road)]  # Ensure paths refer to actual Road objects

    def choose_path(self, traffic_counts):
        """Choose the path with the smallest number of cars."""
        return min(self.paths, key=lambda path: traffic_counts[path])

# Car class
class Car(Vehicle):
    def __init__(self, entrance, exit, paths):
        super().__init__(max_speed=60, entrance=entrance, exit=exit, paths=paths)

# Moped class
class Moped(Vehicle):
    def __init__(self, entrance, exit, paths):
        super().__init__(max_speed=45, entrance=entrance, exit=exit, paths=paths)

# Bus class
class Bus(Vehicle):
    def __init__(self, entrance, exit, path, entrance_time):
        super().__init__(max_speed=40, entrance=entrance, exit=exit, paths=[path])
        self.entrance_time = entrance_time