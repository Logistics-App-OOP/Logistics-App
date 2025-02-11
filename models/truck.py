class Truck:
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
        
    
    
