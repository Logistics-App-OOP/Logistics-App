class Truck:
<<<<<<< HEAD
    def __init__(self, truck_id,brand,capacity,max_range):
        self._truck_id = truck_id
        self._brand = brand
        self._capacity = capacity
        self._max_range = max_range
        self._available = True
        
    @property
    def truck_id(self):
        return self._truck_id
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def capacity(self):
        return self._capacity
    
<<<<<<< HEAD
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Truck capacity cannot be negative.")
        self._capacity = value
    
    @property
    def max_range(self):
        return self._max_range
                    
=======
    @property
    def max_range(self):
        return self._max_range
    
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
    @property
    def available(self):
        return self._available
    
<<<<<<< HEAD
    def assign_to_route(self,route):
=======
    def change_availability_when_assigned(self):
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
        if not self._available:
            raise ValueError("Truck is already assigned to a route!")
        self._available = False
    
    def release(self):
        self._available = True
    
    def __str__(self):
<<<<<<< HEAD
<<<<<<< HEAD
            return f"Truck {self._truck_id}: {self._brand}, Capacity: {self._capacity}kg,Max range:{self._max_range} Available: {self._available}"
=======
        return f"Truck {self._truck_id}: {self._brand}, Capacity: {self._capacity}kg, Available: {self._available}"
    
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
        return f"Truck {self._truck_id}: {self._brand}, Capacity: {self._capacity}kg,Max range:{self._max_range} Available: {self._available}"
    
>>>>>>> 4c07a03 (Created CreateRoute)
=======
    truck_id = 1
    pass
>>>>>>> 272ca14 (uasim's branch)
