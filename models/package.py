from cities import Cities
from package_status import PackageStatus

class Package:
    package_id = 1
    def __init__(self,start_location,end_location,weight,customer_name,customer_phone):
        self._id = Package.package_id
        Package.package_id += 1
        self._start_location = Cities.city_validator(start_location)
        self._end_location = Cities.city_validator(end_location)
        if weight <= 0:
            raise ValueError("Weight cannot be negative.")
        self._weight = weight
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")
        self._customer_name = customer_name
        if not customer_phone:
            raise ValueError("Customer phone cannot be empty.")
        self._customer_phone = str(customer_phone)
        self._status = PackageStatus.RECEIVED
        
    @property
    def id(self):
        return self._id
    
    @property
    def start_location(self):
        return self._start_location

    @property
    def end_location(self):
        return self._end_location

    @property
    def weight(self):
        return self._weight

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def customer_phone(self):
        return self._customer_phone
    
    def update_status(self):
        self._status = PackageStatus.next(self._status)   
    
    def __str__(self):
        return (f"Package {self.id}: {self.start_location} to {self.end_location}\n"
                f"Weight: {self.weight}kg.\n"
                f"Customer: {self.customer_name} ({self.customer_phone})")

pack1 = Package("Sydney", "Melbourne", 45, "Uasim", "0876417576")
print(str(pack1))
        
        
        