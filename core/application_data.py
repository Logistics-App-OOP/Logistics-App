<<<<<<< HEAD

from models.package import Package
from models.route import Route
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from models.locations import Locations
from datetime import datetime
class Application_data:
    
=======
from models.truck import Truck
class ApplicationData:
>>>>>>> 272ca14 (uasim's branch)
    def __init__(self):
        
        self._packages:list[Package] = []
        self._routes: list[Route] = []
<<<<<<< HEAD
<<<<<<< HEAD
        self._trucks: list[Truck] = []
        self._adding_trucks()
=======
=======
from models.employee import Employee
>>>>>>> 4c07a03 (Created CreateRoute)

class Application_data:
    
    def __init__(self):
<<<<<<< HEAD
        self._employees = []
        self._packages = []
        self._routes = []
        self._trucks = self._adding_trucks()
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
        self._employees: list[Employee] = []
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks = []
        self._adding_trucks()
>>>>>>> 4c07a03 (Created CreateRoute)
        self._logged_employee = None
            
    @property
    def employees(self):
        return tuple(self._employees)
    
=======
        self._trucks:list[Truck] = []
=======
        self._trucks:list[Truck] = [
            Truck(1001, "Scania", 42000, 8000),
            Truck(1002, "Scania", 42000, 8000),
            Truck(1003, "Scania", 42000, 8000),
            Truck(1004, "Scania", 42000, 8000),
            Truck(1005, "Scania", 42000, 8000),
            Truck(1006, "Scania", 42000, 8000),
            Truck(1007, "Scania", 42000, 8000),
            Truck(1008, "Scania", 42000, 8000),
            Truck(1009, "Scania", 42000, 8000),
            Truck(1010, "Scania", 42000, 8000),

            Truck(1011, "Man", 37000, 10000),
            Truck(1012, "Man", 37000, 10000),
            Truck(1013, "Man", 37000, 10000),
            Truck(1014, "Man", 37000, 10000),
            Truck(1015, "Man", 37000, 10000),
            Truck(1016, "Man", 37000, 10000),
            Truck(1017, "Man", 37000, 10000),
            Truck(1018, "Man", 37000, 10000),
            Truck(1019, "Man", 37000, 10000),
            Truck(1020, "Man", 37000, 10000),
            Truck(1021, "Man", 37000, 10000),
            Truck(1022, "Man", 37000, 10000),
            Truck(1023, "Man", 37000, 10000),
            Truck(1024, "Man", 37000, 10000),
            Truck(1025, "Man", 37000, 10000),

            Truck(1026, "Actros", 26000, 13000),
            Truck(1027, "Actros", 26000, 13000),
            Truck(1028, "Actros", 26000, 13000),
            Truck(1029, "Actros", 26000, 13000),
            Truck(1030, "Actros", 26000, 13000),
            Truck(1031, "Actros", 26000, 13000),
            Truck(1032, "Actros", 26000, 13000),
            Truck(1033, "Actros", 26000, 13000),
            Truck(1034, "Actros", 26000, 13000),
            Truck(1035, "Actros", 26000, 13000),
            Truck(1036, "Actros", 26000, 13000),
            Truck(1037, "Actros", 26000, 13000),
            Truck(1038, "Actros", 26000, 13000),
            Truck(1039, "Actros", 26000, 13000),
            Truck(1040, "Actros", 26000, 13000)]
        
>>>>>>> e431c9e (update branch)
        
>>>>>>> 272ca14 (uasim's branch)
    @property
    def packages(self):
        return self._packages
    
    @property
    def routes(self):
        return self._routes
    
    @property
    def trucks(self):
        return self._trucks
    
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
>>>>>>> 4c07a03 (Created CreateRoute)
    def create_package(self, customer_name, customer_phone, start_loc, end_loc, weight):
        package = Package(customer_name, customer_phone, start_loc, end_loc, weight)
        self._packages.append(package)
        return package
    
<<<<<<< HEAD
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
    

    def create_employee(self, username, firstname, lastname, password, user_role):
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'Employee username: {username} already exist.')
=======
    def create_route(self, departure_time, start_loc, *next_loc):
        route = Route(departure_time, start_loc, *next_loc)
        self._routes.append(route)
        return route

    def create_employee(self, username, firstname, lastname, password, user_role) -> Employee:
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
<<<<<<< HEAD
                f'Employee {username} already exist.')
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
                f'Employee username: {username} already exist.')
>>>>>>> 4c07a03 (Created CreateRoute)
        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)
        return employee
    
<<<<<<< HEAD
    def find_employee_by_username(self, username: str):
=======
    def find_employee_by_username(self, username: str) -> Employee:
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
        filtered = [user for user in self._employees if user.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}!')
        return filtered[0]
    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in user.')

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None
    
    def login(self, employee: Employee):
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None
<<<<<<< HEAD
        
    def check_truck_has_enough_range_and_is_available(self, total_distance):
        suitable_trucks = [truck for truck in self.trucks if truck.available and truck.max_range >= total_distance]
        if not suitable_trucks:
            raise ValueError(f"Truck with range {total_distance}km does not exist.")
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
                result += f"Next stop: {route.next_stop(current_time)}"
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
        available_trucks = []
        result = "\nTrucks:\n"
        
        for truck in self.trucks:
            assigned_route = None
            available_time = "Available"
            available_time += "\n"
            for route in self.routes:
                if route.assigned_truck == truck:
                    assigned_route = route
                    available_time = f"Will be available on {route.arrival_times[-1].strftime('%b %d %H:%M')}\n"
                    break
                
            result += f"Truck {truck.truck_id}: {truck.brand}, Capacity: {truck.capacity}kg, Max Range: {truck.max_range}km.\n"
            if assigned_route:
                result += f"Assigned to Route {assigned_route.id} - {available_time}\n"
            else:
                result += "Available\n"
                result += "\n"
                available_trucks.append(truck)
                
        if not available_trucks:
            return "No trucks available."
        
        return result
    
=======
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
    
    def _adding_trucks(self):
        for truck_id in range(1001,1011):
            self._trucks.append(Truck(truck_id,"Scania", 42000,8000))
            
        for truck_id in range(1011,1026):
            self._trucks.append(Truck(truck_id,"Man",37000,10000))
            
        for truck_id in range(1026,1041):
            self._trucks.append(Truck(truck_id,"Actros", 26000, 13000))
=======
    def add_package(self,package):
        self.packages.append(package)
>>>>>>> 272ca14 (uasim's branch)
        
    def add_route(self,route):
        self.routes.append(route)
        
    def add_truck(self,truck):
        self.trucks.append(truck)
        
    def get_package(self,pack_id):
        for package in self.packages:
            if package.package_id == pack_id:
                return package
        raise ValueError("Package does not exist!")
    
    def get_route(self,id_route):
        for route in self.routes:
            if route.route_id == id_route:
                return route
        raise ValueError("Route does not exist!")
    
    def get_truck(self,id_truck):
        for truck in self.trucks:
            if truck.truck_id == id_truck:
                return truck
        raise ValueError("Truck does not exist!")
    
    
        


    # def __init__(self):
    #     self._users = []
    #     self._logged_user = None

    # @property
    # def users(self):
    #     return tuple(self._users)

    # def create_user(self, username, firstname, lastname, password, user_role) -> User:
    #     if len([u for u in self._users if u.username == username]) > 0:
    #         raise ValueError(
    #             f'User {username} already exist. Choose a different username!')

    #     user = User(username, firstname, lastname, password, user_role)
    #     self._users.append(user)

    #     return user

    # def find_user_by_username(self, username: str) -> User:
    #     filtered = [user for user in self._users if user.username == username]
    #     if filtered == []:
    #         raise ValueError(f'There is no user with username {username}!')

    #     return filtered[0]

    # @property
    # def logged_in_user(self):
    #     if self.has_logged_in_user:
    #         return self._logged_user
    #     else:
    #         raise ValueError('There is no logged in user.')

    # @property
    # def has_logged_in_user(self):
    #     return self._logged_user is not None

    # def login(self, user: User):
    #     self._logged_user = user

    # def logout(self):
    #     self._logged_user = None
=======
from models.truck import Truck
from models.employee import Employee
from models.package import Package
from models.route import Route

class Application_data:
    
    def __init__(self):
        self._employees = []
        self._packages = []
        self._routes = []
        self._trucks = self._adding_trucks()
        self._logged_employee = None
            
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
    

    def create_package(self, customer_name, customer_phone, start_loc, end_loc, weight):
        package = Package(customer_name, customer_phone, start_loc, end_loc, weight)
        self._packages.append(package)
        return package
    
    def create_route(self, departure_time, start_loc, *next_loc):
        route = Route(departure_time, start_loc, *next_loc)
        self._routes.append(route)
        return route

    def create_employee(self, username, firstname, lastname, password, user_role) -> Employee:
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'Employee {username} already exist.')
        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)
        return employee
    
    def find_employee_by_username(self, username: str) -> Employee:
        filtered = [user for user in self._employees if user.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}!')
        return filtered[0]
    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in user.')

    @property
    def has_logged_in_employee(self):
        return self._logged_employee is not None
    
    def login(self, employee: Employee):
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None
    
    def _adding_trucks(self):
        for truck_id in range(1001,1011):
            self._trucks.append(Truck(truck_id,"Scania", 42000,8000))
            
        for truck_id in range(1011,1026):
            self._trucks.append(Truck(truck_id,"Man",37000,10000))
            
        for truck_id in range(1026,1041):
            self._trucks.append(Truck(truck_id,"Actros", 26000, 13000))
        
    
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
