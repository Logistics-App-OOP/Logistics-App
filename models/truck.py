class Truck:
<<<<<<< HEAD
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
=======
    truck_id = 1
    pass
=======
    def __init__(self, truck_id: int, model: str, capacity: int, max_range: int):
        self._truck_id = truck_id
        self._model = model
        self._capacity = capacity
        self._max_range = max_range
        self.available = True
        
    @property
    def truck_id(self):
        return self._truck_id
    
    @property
    def model(self):
        return self._model
    
    @property 
    def capacity(self):
        return self._capacity
    
    @property
    def max_range(self):
        return self._max_range
    
    def assign_to_route(self):
        if not self.available:
            raise ValueError(f"Truck {self.id} is not available.")
        self.available = False
        
    def unassign_truck(self):
        self.available = True
        
    def __str__(self):
        return f"Truck available: {self.available}.\nTruck id: {self.truck_id}.\nTruck model:{self.model}.\nTruck capacity: {self.capacity}kg.\nTruck max range: {self.max_range}km."
        
            
            
truck1 = Truck(1010,"MAN",40000,20000)

print(truck1)
        
    
    
>>>>>>> 6cabb68 (update branch)
>>>>>>> e431c9e (update branch)
