from models.locations import Locations
from datetime import timedelta

class Route:

    ID = 0
    AVERAGE_SPEED_KMH = 87  # km/h
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
    }


    def __init__(self, departure_time, start_loc, *next_loc):
        all_locations = [start_loc] + list(next_loc)
        if not all(self.is_valid_location(loc) for loc in all_locations):
            invalid = [loc for loc in all_locations if loc.upper().replace(" ", "_") not in Locations.__members__]
            raise ValueError(f"Invalid locations: {', '.join(invalid)}")
        self.locations = [Locations[loc.upper().replace(" ", "_")] for loc in all_locations]
        self.all_locations = all_locations
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
            start = self.locations[i].value
            end = self.locations[i + 1].value
            distance = self.DISTANCES.get((start, end)) or self.DISTANCES.get((end, start))

            if distance is None:
                raise ValueError(f"Distance between {start} and {end} not found.")

            # Calculate travel time in hours
            travel_hours = distance / self.AVERAGE_SPEED_KMH
            current_time += timedelta(hours=travel_hours)  # Adding timedelta to datetime object
            times.append(current_time)

        return times

    def __str__(self):
        route_str = []
        for i, loc in enumerate(self.locations):
            time_str = self.arrival_times[i].strftime("%b %d %H:%M")
            route_str.append(f"{loc.value} ({time_str})")

        return " → ".join(route_str)
    
    @staticmethod
    def is_valid_location(loc):
        return loc.upper().replace(" ", "_") in Locations.__members__