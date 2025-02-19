from models.locations import Locations
class Package:
    """
    Represents a Package with an ID number, customer name, customer phone, starting location, delivery location and total weight.
    """
    ID = 1
    def __init__(self, customer_name, customer_phone, start_loc, end_loc, weight):
        """
        Initializes an instance of the class Package.

        Args:
        customer_name (str)
        customer_phone (str)
        start_loc (str)
        end_loc (str)
        weight (int)

        Raises:
        ValueError: if an invalid location (start_loc, end_loc) is provided.
        ValueError: if an invalid mobile number (Australian standard) is provided.
        ValueError: if an invalid package weight (e.g. negative number) is provided.
        """
        if start_loc not in Locations.locations:
            raise ValueError(f"Invalid start location: {start_loc}")
        self._start_loc = start_loc
        if end_loc not in Locations.locations:
            raise ValueError(f"Invalid end location: {end_loc}")
        self._end_loc = end_loc
        self.customer_name = customer_name
        if not customer_phone.isdigit():
            raise ValueError("Phone number must contain only digits!")
        if len(customer_phone) != 10:  
            raise ValueError("Phone number must be exactly 10 digits long!")
        self.customer_phone = customer_phone
        if int(weight) <= 0:
            raise ValueError("The weight of a package can't be a negative number.")
        self.weight = weight
        self.id = Package.ID
        Package.ID += 1
        self.status = "Created"
    
    @property
    def start_loc(self):
        return self._start_loc
    
    @property
    def end_loc(self):
        return self._end_loc
    
    def update_status(self):
        if self.status == "Created":
            self.status = "In Transit"
    
