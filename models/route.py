from models.locations import Locations
from datetime import timedelta,datetime

class Route:

    ID = 1
    AVERAGE_SPEED_KMH = 87
    DISTANCES = {
        ("Sydney", "Melbourne"): 877,
        ("Melbourne", "Adelaide"): 725,
        ("Adelaide", "Alice Springs"): 1530,
        ("Alice Springs", "Brisbane"): 2993,
        ("Brisbane", "Darwin"): 3426,
        ("Darwin", "Perth"): 4025,
        ("Perth", "Sydney"): 4016,
        ("Sydney", "Brisbane"): 909,
        ("Melbourne", "Brisbane"): 1765,
        ("Adelaide", "Perth"): 2785,
        ("Alice Springs", "Darwin"): 1497,
        ("Melbourne", "Perth"): 3509,
        ("Brisbane", "Adelaide"): 1927,
        ("Sydney", "Adelaide"): 1376,
        ("Sydney", "Alice Springs"): 2762,
        ("Sydney", "Darwin"): 3935,
        ("Melbourne", "Alice Springs"): 2255,
        ("Melbourne", "Darwin"): 3752,
        ("Adelaide", "Darwin"): 3027,
        ("Alice Springs", "Perth"): 2481,
        ("Brisbane", "Perth"): 4311}


    def __init__(self, departure_time :datetime, start_loc, *next_loc):
        all_locations = [start_loc] + list(next_loc)
        valid_locations = [loc for loc in all_locations if loc in Locations.locations]        
        self.locations = valid_locations
        self.id = self.id_counter()
        self.departure_time = departure_time
        self.arrival_times = self._calculate_arrival_times()

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
        
        return " -> ".join(route_str)
<<<<<<< HEAD
    
<<<<<<< HEAD
    
                
                
        
        
    
        
        
             
        
<<<<<<< HEAD
        return " -> ".join(route_str)
<<<<<<< HEAD
    
    @staticmethod
    def is_valid_location(loc):
        return loc.upper().replace(" ", "_") in Locations.__members__
=======
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
<<<<<<< HEAD
=======
        

    















#     creating a delivery route – should have a unique id, and a list of locations (at least two).
# The first location is the starting location – it has a departure time.
# The other locations have expected arrival time.
>>>>>>> 272ca14 (uasim's branch)
=======
    @staticmethod
    def is_valid_location(loc):
        return loc.upper().replace(" ", "_") in Locations.__members__
>>>>>>> 24a6a4e (Updated main based on Emil's branch)
=======
>>>>>>> e6a5d05 (Created truck editted app_data, route,package)
