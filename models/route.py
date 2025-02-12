from models.locations import Locations

class Route:

    ID = 1

    def __init__(self, start_loc, *next_loc):
        all_locations = [start_loc] + list(next_loc)
        if not all(self.is_valid_location(loc) for loc in all_locations):
            invalid = [loc for loc in all_locations if loc.upper().replace(" ", "_") not in Locations.__members__]
            raise ValueError(f"Invalid locations: {', '.join(invalid)}")
        self.locations = [Locations[loc.upper().replace(" ", "_")] for loc in all_locations]
        self.id = self.id_counter()

    @classmethod
    def id_counter(cls):
        cls.ID += 1
        return cls.ID
    
    @staticmethod
    def is_valid_location(loc):
        return loc.upper().replace(" ", "_") in Locations.__members__

    def __str__(self):
        return " → ".join(loc.value for loc in self.locations)