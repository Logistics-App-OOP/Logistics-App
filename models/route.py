from models.package import Package
from models.locations import Locations
from datetime import timedelta,datetime
from models.truck import Truck

class Route:
    """
    Represents a route with an ID number, departure time, a starting location, all the next locations, a list of packages assigned to it.
    Speed and distances inbetween cities are held constant.
    """
    ID = 1
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
        """
        Initializes an instance of the Route class.
        
        Args:
        departure_time (datetime): A formatted date string (e.g., "2025-02-11T14:30").
        start_loc (str): The starting location, must be a valid system-supported location.
        *next_loc (str): Additional locations forming the route, must also be valid locations.
        
        Raises:
        ValueError: If an invalid location is provided.
        """
        all_locations = [start_loc] + list(next_loc)
        valid_locations = [loc for loc in all_locations if loc in Locations.locations]        
        self.locations = valid_locations
        self.id = Route.ID
        Route.ID += 1
        self.departure_time = departure_time
        self.arrival_times = self._calculate_arrival_times()
        self.assigned_truck = None
        self.packages: list[Package] = []
        
    def total_distance(self):
        """
        Calculates the total distance of the route in kilometers. Sums location A to location B to location C, based on the
        provided constants.
        """
        total_distance = 0
        for i in range(len(self.locations)-1):
            start = self.locations[i]
            end = self.locations[i + 1]
            distance = self.DISTANCES.get((start, end)) or self.DISTANCES.get((end, start))
            if distance is None:
                raise ValueError(f"There is no route from {start} to {end}.")
            total_distance += distance
        return total_distance
            
    def assign_truck(self,truck: Truck):
        """
        Assigns a truck to a route. Changes self.assigned_truck from None to the designated object of the Class Truck.

        Args: 
        truck (Truck) - the instance of the class Truck that we're assigning to the route.

        Raises:
        ValueError: if the route already has a truck assigned to it.
        """
        if self.assigned_truck:
            raise ValueError(f"Route {self.id} has a truck {self.assigned_truck} already assigned")
        self.assigned_truck:Truck = truck
    
    def assign_package(self,package: Package):
        """
        Appends a package to the collection of packages on the route.

        Args:
        package (Package) - the instance of the class Package that we're appending to self.packages.

        """
        self.packages.append(package)
    
    def _calculate_arrival_times(self):
        """
        Calculates the arrival times for each location based on the provided constants for average speed and distances between
        locations.

        Returns:
        times (list): list of datetime objects.

        """
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
    
    def current_stop(self,current_time):
        """
        Returns current_stop based on current_time.

        Args:
        current_time (datetime)

        Returns:
        str: the name of the current stop.

        """
        for i in range(len(self.arrival_times)):
            if current_time < self.arrival_times[i]:
                return self.locations[i-1]
        return self.locations[-1]
    
    def next_stop(self,current_time):
        """
        Returns next_stop based on current_time.

        Args:
        current_time (datetime)

        Returns:
        str: the name of the next stop.

        """
        for i in range(len(self.arrival_times)):
            if current_time < self.arrival_times[i]:
                return self.locations[i]
        return self.locations[-1]
    
    def __str__(self):
        route_str = []
    
        for i in range(len(self.locations)):
            loc = self.locations[i]
            time_str = self.arrival_times[i].strftime("%b %d %H:%M")
            route_str.append(f"{loc} ({time_str})")
        
        return f"Route {self.id} -> {' -> '.join(route_str)}"
    
    
