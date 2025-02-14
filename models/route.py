from tkinter import NO
from models.locations import Locations
from datetime import timedelta,datetime

class Route:

    ID = 0
    AVERAGE_SPEED_KMH = 87
    DISTANCES = {
        ("Sydney", "Melbourne"): 877,
        ("Melbourne", "Adelaide"): 725,
        ("Adelaide", "AliceSprings"): 1530,
        ("AliceSprings", "Brisbane"): 2993,
        ("Brisbane", "Darwin"): 3426,
        ("Darwin", "Perth"): 4025,
        ("Perth", "Sydney"): 4016,
        ("Sydney", "Brisbane"): 909,
        ("Melbourne", "Brisbane"): 1765,
        ("Adelaide", "Perth"): 2785,
        ("AliceSprings", "Darwin"): 1497,
        ("Melbourne", "Perth"): 3509,
        ("Brisbane", "Adelaide"): 1927,
        ("Sydney", "Adelaide"): 1376,
        ("Sydney", "AliceSprings"): 2762,
        ("Sydney", "Darwin"): 3935,
        ("Melbourne", "AliceSprings"): 2255,
        ("Melbourne", "Darwin"): 3752,
        ("Adelaide", "Darwin"): 3027,
        ("AliceSprings", "Perth"): 2481,
        ("Brisbane", "Perth"): 4311}


    def __init__(self, departure_time :datetime, start_loc, *next_loc):
        all_locations = [start_loc] + list(next_loc)
        valid_locations = [loc for loc in all_locations if loc in Locations.locations]        
        self.locations = valid_locations
        self.id = self.id_counter()
        self.departure_time = departure_time
        self.arrival_times = self._calculate_arrival_times()
        self.assigned_truck = None
        
    def total_distance(self):
        total_distance = 0
        for i in range(len(self.locations)-1):
            start = self.locations[i]
            end = self.locations[i + 1]
            distance = self.DISTANCES.get((start, end)) or self.DISTANCES.get((end, start))
            if distance is None:
                raise ValueError(f"There is no route from {start} to {end}.")
            total_distance += distance
        return total_distance
            
    def assign_truck(self,truck):
        if self.assigned_truck:
            raise ValueError(f"Route {self.id} has a truck {self.assigned_truck} already assigned")
        self.assigned_truck = truck

    @classmethod
    def id_counter(cls):
        cls.ID += 1
        return cls.ID
    
    def _calculate_arrival_times(self):
        times = [self.departure_time]
        current_time = self.departure_time

        for i in range(len(self.locations) - 1):
            start = self.locations[i]
            end = self.locations[i + 1]
            distance = self.DISTANCES.get((start, end)) or self.DISTANCES.get((end, start))

            travel_hours = distance / self.AVERAGE_SPEED_KMH
            current_time += timedelta(hours=travel_hours)
            times.append(current_time)

        return times

    def __str__(self):
        route_str = []
    
        for i in range(len(self.locations)):
            loc = self.locations[i]
            time_str = self.arrival_times[i].strftime("%b %d %H:%M")
            route_str.append(f"{loc} ({time_str})")
        
        return f"Route {self.id} -> " + " -> ".join(route_str)
