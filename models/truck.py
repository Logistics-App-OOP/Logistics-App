class Truck:
    def __init__(self, truck_id,brand,capacity,max_range):
        """
        Represents a Truck with an ID number, brand, weight capacity, maximum kilometer range, availability status.
        """
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

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Truck capacity cannot be negative.")
        self._capacity = value

    @property
    def max_range(self):
        return self._max_range

    @property
    def available(self):
        return self._available

    def assign_to_route(self,route):
        """
        Changes truck availablity from True to False. 

        Args: 
        route (instance of the Class Route)

        Returns: 
        str: A message warning if the truck is already unavailable.
        """
        if not self._available:
            raise ValueError("Truck is already assigned to a route!")
        self._available = False

    def release(self):
        """
        Changes truck availablity from False to True. 
        """
        self._available = True

    def __str__(self):
        return f"Truck: {self.truck_id}, Available: {self.available}."







