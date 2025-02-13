from models.locations import Locations
class Package:
    
    ID = 0
    def __init__(self, customer_name, customer_phone, start_loc, end_loc, weight):
        self.customer_name = customer_name
        self.customer_phone = Package.validate_phone(customer_phone)
        self._start_loc = Locations(start_loc)
        self._end_loc = Locations(end_loc)
        self.weight = Package.validate_weight(weight)
        self.id = self.id_counter()
        self.status = "Created"
    
    @classmethod
    def id_counter(cls):
        cls.ID += 1
        return cls.ID
    
    @property
    def start_loc(self):
        return self._start_loc
    
    @property
    def end_loc(self):
        return self._end_loc
    
    def update_status(self):
        if self.status == "Created":
            self.status = "In Transit"
        elif self.status == "In Transit":
            self.status = "Delivered"

    @staticmethod
    def validate_phone(phone):
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits!")
        if len(phone) != 10:  
            raise ValueError("Phone number must be exactly 10 digits long!")
        if not (phone.startswith("04") or phone.startswith(("02", "03", "07", "08"))):
            raise ValueError("Phone number must start with 04 (mobile) or a valid area code (02, 03, 07, 08)!")
        return phone
    
    @staticmethod
    def validate_weight(weight):
        if int(weight) <= 0:
            raise ValueError("The weight of a package can't be a negative number.")
        return weight
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
    
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
    
>>>>>>> 4c07a03 (Created CreateRoute)
