from cities import Cities
from models.customer import Customer
from package_status import PackageStatus

class Package:
    package_id = 1

    def __init__(self,start_location,end_location,weight, customer_name, customer_surname, customer_phone):
        self._id = Package.package_id
        Package.package_id += 1
        self._start_location = Cities.city_validator(start_location)
        self._end_location = Cities.city_validator(end_location)
        if weight <= 0:
            raise ValueError("Weight must be at least 1 kg.")
        self._weight = weight
        self._customer_info = Customer(customer_name,customer_surname, customer_phone)
        self._status = PackageStatus.RECEIVED


    @property
    def id(self):
        return self._id

    @property
    def start_location(self):
        return self._start_location.capitalize()

    @property
    def end_location(self):
        return self._end_location.capitalize()

    @property
    def weight(self):
        return self._weight

    @property
    def customer_info(self):

        return str(Customer)


    def update_status(self):
        self._status = PackageStatus.next(self._status)

    def __str__(self):
        return (f"Package ID:({self.id}), From {self.start_location} to {self.end_location}.\n"
                f"Weight: {self.weight}kg.\n"
                f"{self._customer_info}")






pak = Package('sydney', 'melbourne', 100, 'Gosho', 'Petrov', '08999999')
pak1 = Package('sydney', 'melbourne', 100, 'Gosho', 'Sashov', '08999999')
pak2 = Package('sydney', 'melbourne', 100, 'Gosho', 'Petkov', '08999999')

print(pak)
print(pak1)
print(pak2)