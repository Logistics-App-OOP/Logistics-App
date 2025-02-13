from models.package import Package


class Truck:

    def __init__(self, name, capacity, max_range, first_id, count):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.all_truck_ids = list(range(first_id, first_id + count))
        self.free_truck_ids = [id for id in self.all_truck_ids]
        self._truck_packages: list[Package] = []
    
    def add_package_to_truck(self, package):
        self._truck_packages.append(package)