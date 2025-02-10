import datetime
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
    
    def get_distance(self,from_where,to_where):
        for city1,city2,dist in self.DISTANCES:
            if (city1, city2) == (from_where, to_where) or (city2, city1) == (from_where, to_where):
                return dist
        return None        
        
<<<<<<< HEAD
        return " -> ".join(route_str)
<<<<<<< HEAD
    
    @staticmethod
    def is_valid_location(loc):
        return loc.upper().replace(" ", "_") in Locations.__members__
=======
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
        

    















#     creating a delivery route – should have a unique id, and a list of locations (at least two).
# The first location is the starting location – it has a departure time.
# The other locations have expected arrival time.
>>>>>>> 272ca14 (uasim's branch)
