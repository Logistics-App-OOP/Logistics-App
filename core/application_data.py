from models.truck import Truck
from models.employee import Employee
from models.package import Package
from models.route import Route
from models.locations import Locations
from datetime import datetime
class Application_data:
    
    def __init__(self):
        self._employees: list[Employee] = []
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []
        self._adding_trucks()
        self._logged_employee = None
        
    def save_data(self):

        with open("text_files/employees.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "firstname", "lastname", "password", "role"])
            for emp in self._employees:
                writer.writerow([emp.username, emp.firstname, emp.lastname, emp.password, emp.role])

        with open("text_files/trucks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["truck_id", "brand", "capacity", "max_range", "available"])
            for truck in self._trucks:
                writer.writerow([truck.truck_id, truck.brand, truck.capacity, truck.max_range, truck.available])

        with open("text_files/packages.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "customer_name", "phone", "start_loc", "end_loc", "weight", "status"])
            for package in self._packages:
                writer.writerow([package.id, package.customer_name, package.customer_phone, package.start_loc, package.end_loc, package.weight, package.status])

        with open("text_files/routes.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "locations", "departure_time", "assigned_truck", "packages", "arrival_times"])
            for route in self._routes:
                writer.writerow([
                    route.id,
                    "|".join(route.locations),
                    route.departure_time.strftime("%Y-%m-%dT%H:%M"),
                    route.assigned_truck.truck_id if route.assigned_truck else "",
                    "|".join(str(p.id) for p in route.packages),
                    "|".join(time.strftime("%Y-%m-%dT%H:%M") for time in route.arrival_times)
                ])

    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    @property
    def routes(self):
        return tuple(self._routes)
    
    @property
    def trucks(self):
        return tuple(self._trucks)
    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in user.')

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None
    
    def _adding_trucks(self):
        if self.trucks:
            return
        for truck_id in range(1001,1011):
            self._trucks.append(Truck(truck_id,"Scania", 42000,8000))
            
        for truck_id in range(1011,1026):
            self._trucks.append(Truck(truck_id,"Man",37000,10000))
            
        for truck_id in range(1026,1041):
            self._trucks.append(Truck(truck_id,"Actros", 26000, 13000))
        
    
    def create_package(self, customer_name, customer_phone, start_loc, end_loc, weight):
        package = Package(customer_name, customer_phone, start_loc, end_loc, weight)
        self._packages.append(package)
        return package
         
    def find_package_by_id(self,package_id):
        for package in self.packages:
            if package.id == package_id:
                return package
        raise ValueError(f"Package with ID: {package_id} does not exist.")
                    
    def create_route(self, departure_time, start_loc, *next_loc):
        all_locations = [start_loc] + list(next_loc)
        invalid_locations = [loc for loc in all_locations if loc not in Locations.locations]
        if invalid_locations:
            raise ValueError(f"Invalid locations: {', '.join(invalid_locations)}")
        route = Route(departure_time, start_loc, *next_loc)
        self._routes.append(route)
        return route
    
    def find_route_by_id(self,route_id):
        for route in self.routes:
            if route.id == route_id:
                return route
        raise ValueError(f"Route with id {route_id} does not exist.")
    
    def update_package_and_truck_status_when_route_is_finished(self):
        current_time = datetime.now()
        for route in self.routes:
            if route.arrival_times[-1] <= current_time:
                for package in route.packages:
                    if package.status == "In Transit":
                        package.status = "Delivered"
                if route.assigned_truck:
                    route.assigned_truck.release()
                    route.assigned_truck = None

    def create_employee(self, username, firstname, lastname, password, user_role):
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'Employee username: {username} already exist.')
        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)
        return employee
    
    def find_employee_by_username(self, username: str):
        filtered = [user for user in self._employees if user.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}!')
        return filtered[0]
    
    def login(self, employee: Employee):
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None
        
    def check_truck_has_enough_range_and_is_available(self, total_distance):
        suitable_trucks = [truck for truck in self.trucks if truck.available and truck.max_range >= total_distance]
        if not suitable_trucks:
            raise ValueError(f"Truck with range {total_distance}km does not exist or not available.")
        return suitable_trucks[0]
    
    def view_routes_in_progress(self):
        self.update_package_and_truck_status_when_route_is_finished()
        if not self.routes:
            return "No routes available!"
        current_time = datetime.now()
        result = "\nRoutes in progress:\n"
        for route in self.routes:
            if route.departure_time <= current_time < route.arrival_times[-1]:
                if route.assigned_truck:
                    truck_info = route.assigned_truck.truck_id
                else:
                    truck_info = "No truck assigned to route."
                if route.packages:
                    asgn_packages = [f"Package id: {package.id} {package.status}" for package in route.packages]
                    weight = sum(int(package.weight) for package in route.packages)
                else:
                    asgn_packages = ["No packages assigned"]
                    weight = 0
                asgn_packages = [f"ID: {package.id}" for package in route.packages] if route.packages else ["No packages assigned"]
                result += f"Route {route.id}: {' -> '.join(route.locations)}\n"
                result += f"Truck: {truck_info}\n"
                result += f"Assigned packages: {'-'.join(asgn_packages)}\n"
                result += f"Total weight: {weight}\n"
                result += f"Departure time: {route.departure_time}\n"
                result += f"Last stop: {route.current_stop(current_time)}\n"
                result += f"Next stop: {route.next_stop(current_time)}\n"
                result += "\n"
        return result
    
    def view_unassigned_packages(self):
        unassigned_packages: list[Package] = []
        for package in self.packages:
            for route in self.routes:
                if package in route.packages:
                    break
            else:
                unassigned_packages.append(package)
        if not unassigned_packages:
            return "No unassigned packages"
        
        result = "Unassigned packages:\n"
        for package in unassigned_packages:
            result += f"Package {package.id} is at Location: {package.start_loc}.\n"
        return result
        
    def view_trucks(self):
        self.update_package_and_truck_status_when_route_is_finished()
        has_available_truck = False
        result = "\nTrucks:\n"
        
        for truck in self.trucks:
            assigned_route = None
            available_time = "Available"
            available_time += "\n"
            for route in self.routes:
                if route.assigned_truck == truck:
                    assigned_route = route
                    break
                
            result += f"Truck {truck.truck_id}: {truck.brand}, Capacity: {truck.capacity}kg, Max Range: {truck.max_range}km.\n"
            if assigned_route:
                current_time = datetime.now()
                if assigned_route.departure_time > current_time:
                    available_time = assigned_route.departure_time.strftime("%Y-%m-%d-%H:%M")
                    result += f"Assigned to Route {assigned_route.id} - Will be available until {available_time}.\n"
                    result += "\n"
                else:
                    available_time = assigned_route.arrival_times[-1].strftime("%Y-%m-%d-%H:%M")
                    result += f"Assigned to Route {assigned_route.id} - Will be available after {available_time}.\n"
                    result += "\n"
            else:
                has_available_truck = True
                result += "Available\n"
                result += "\n"
                
        if not has_available_truck:
            return "No trucks available."
        
        return result
    
    
