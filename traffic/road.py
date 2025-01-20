# Road class
class Road:
    def __init__(self, length, start_intersection, end_intersection):
        self.length = length
        self.start_intersection = start_intersection
        self.end_intersection = end_intersection
        self.vehicles = []

        # Connect this road to the start and end intersections
        start_intersection.connect_road(self)
        end_intersection.connect_road(self)