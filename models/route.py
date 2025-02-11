from datetime import datetime, timedelta
from models.package import Package
from models.truck import Truck
from core.application_data import ApplicationData
class Route:
    route_id = 1
    AVERAGE_SPEED_KMH = 87
    DISTANCES = [
    ("Sydney", "Melbourne", 877), ("Sydney", "Adelaide", 1376), ("Sydney", "Alice Springs", 2762),
    ("Sydney", "Brisbane", 909), ("Sydney", "Darwin", 3935), ("Sydney", "Perth", 4016),
    ("Melbourne", "Adelaide", 725), ("Melbourne", "Alice Springs", 2255), ("Melbourne", "Brisbane", 1765),
    ("Melbourne", "Darwin", 3752), ("Melbourne", "Perth", 3509),("Adelaide", "Alice Springs", 1530),
    ("Adelaide", "Brisbane", 1927), ("Adelaide", "Darwin", 3027),("Adelaide", "Perth", 2785),
    ("Alice Springs", "Brisbane", 2993), ("Alice Springs", "Darwin", 1497), ("Alice Springs", "Perth", 2481),
    ("Brisbane", "Darwin", 3426), ("Brisbane", "Perth", 4311),("Darwin", "Perth", 4025)]

    def __init__(self,locations: list[str], departure_time: str):
        if len(locations) < 2:
            raise ValueError("A route must have at least two locations.")
        self.locations = locations
        self.departure_time = datetime.strptime(departure_time, "%b %d %H:%M")
        self._id = Route.route_id
        Route.route_id += 1
        self.assigned_packages:list[Package] = []
        self.assigned_truck = None
    
    def get_distance(self,from_where,to_where):
        for city1,city2,dist in self.DISTANCES:
            if (city1, city2) == (from_where, to_where) or (city2, city1) == (from_where, to_where):
                return dist
        return None   
    
    def calculate_estimated_arrival_times(self):
        arrival_times = {}
        current_time = self.departure_time
        arrival_times[self.locations[0]] = current_time
        for i in range(1,len(self.locations)):
            city_a = self.locations[i-1]
            city_b = self.locations[i]
            distance = self.get_distance(city_a,city_b)
            if distance is None:
                raise ValueError("No route available!")
            
            total_travel_hours = distance/self.AVERAGE_SPEED_KMH
            travel_time = timedelta(hours=total_travel_hours)
            current_time += travel_time
            arrival_times[city_b] = current_time
        return arrival_times
    
    def assign_package_to_route(self,package:Package):
        if package.start_location not in self.locations:
            raise ValueError(f"There are no routes from {package.start_location}.")
        if package.end_location not in self.locations:
            raise ValueError(f"There are no routes to {package.end_location}.")
        self.assigned_packages.append(package)
        
    def assign_truck_to_route(self):
        app_data = ApplicationData()
        total_distance = 0
        for i in range(len(self.locations) - 1):
            city_a = self.locations[i]
            city_b = self.locations[i+1]
            distance = self.get_distance(city_a, city_b)
            if distance is not None:
                total_distance += distance
                        
        total_package_weight = sum(package.weight for package in self.assigned_packages)
        for truck in app_data.trucks:
            if truck.capacity >= total_package_weight and truck.max_range >= total_distance and truck.available:
                self.assigned_truck = truck
                truck.assign_to_route()
                return f"{truck} assigned to route {self.route_id}."
        raise ValueError("No available truck meets the requirements.")
    
    
                
                
        
        
    
        
        
             
        
        

    















#     creating a delivery route – should have a unique id, and a list of locations (at least two).
# The first location is the starting location – it has a departure time.
# The other locations have expected arrival time.
