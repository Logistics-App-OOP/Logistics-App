from models.truck import Truck

class TruckCarPark:

    SCANIA = "Scania"
    MAN = "Man"
    ACTROS = "Actros"

    CAP_SCANIA = 42_000
    CAP_MAN = 37_000
    CAP_ACTROS = 26_000

    SCANIA_ID = 1001
    MAN_ID = 1011
    ACTROS_ID = 1026

    SCANIA_MAX_RANGE = 8000
    MAN_MAX_RANGE = 10_000
    ACTROS_MAX_RANGE = 26_000

    SCANIA_TRUCK_COUNT = 10
    MAN_TRUCK_COUNT = 15
    ACTROS_TRUCK_COUNT = 15
    
    def __init__(self):
        self.truck_types: list[Truck] = [
            Truck(self.SCANIA, self.CAP_SCANIA, self.SCANIA_MAX_RANGE, self.SCANIA_ID, self.SCANIA_TRUCK_COUNT),
            Truck(self.MAN, self.CAP_MAN, self.MAN_MAX_RANGE, self.MAN_ID, self.MAN_TRUCK_COUNT),
            Truck(self.ACTROS, self.CAP_ACTROS, self.ACTROS_MAX_RANGE, self.ACTROS_ID, self.ACTROS_TRUCK_COUNT)
        ]
    
    def list_all_free_trucks(self):
        free_trucks = []
        for truck_type in self.truck_types:
            free_trucks.extend(truck_type.free_truck_ids)
        return free_trucks
    
    def find_truck_by_id(self, truck_id: int):
        for truck_type in self.truck_types:
            if truck_id in truck_type.free_truck_ids:
                return truck_type