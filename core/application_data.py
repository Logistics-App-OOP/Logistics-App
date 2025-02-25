from models.truck import Truck
from models.employee import Employee
from models.package import Package
from models.route import Route
from models.locations import Locations
from datetime import datetime
import csv

class Application_data:
    
    def __init__(self):
        self._employees: list[Employee] = [Employee("Uasim1702","Uasim","Halak","123456789", "Manager"),
                                            Employee("Lyubo123","Lyubo","Parvanov","987654321", "Manager"),
                                            Employee("Emo123","Emil","Mihaylov","123454321", "Manager")
                                            ]
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks: list[Truck] = []
        self._adding_trucks()
        self._logged_employee = None
        
    def update_package_and_truck_status_when_route_is_finished(self):
        """
        updates the package status from Created to In Transit and from In Transit to Delivered and unassigns truck from route and makes truck 
        available if the time of the last stop of the route has passed.
        """
        current_time = datetime.now()
        for route in self.routes:
            if route.arrival_times[-1] <= current_time:
                for package in route.packages:
                    if package.status == "In Transit":
                        package.status = "Delivered"
                if route.assigned_truck:
                    for truck in self.trucks:
                        if truck.truck_id == route.assigned_truck.truck_id:
                            route.assigned_truck.capacity = truck.capacity
                            break
                    route.assigned_truck.release()
                    route.assigned_truck = None
                    
            elif route.departure_time <= current_time:
                for package in route.packages:
                    if package.status == "Created":
                        package.status = "In Transit"
                        
    def save_data(self):

        with open("text_files/employees.csv","w") as file:
            writer = csv.writer(file)
            for emp in self.employees:
                writer.writerow([emp.username,emp.firstname,emp.lastname,emp.password,emp.role])
                
        with open("text_files/trucks.csv","w") as file:
            writer = csv.writer(file)
            for truck in self.trucks:
                writer.writerow([truck.truck_id,truck.brand,truck.capacity,truck.max_range,truck.available])
                
        with open("text_files/packages.csv","w") as file:
            writer = csv.writer(file)
            for package in self.packages:
                writer.writerow([package.id,package.customer_name,package.customer_phone,package.start_loc,package.end_loc,package.weight,package.status])
        
        with open("text_files/routes.csv", "w") as file:
            writer = csv.writer(file)
            for route in self._routes:
                writer.writerow([route.id,"->".join(route.locations),route.departure_time.strftime("%Y-%m-%d-%H:%M"),
                                route.assigned_truck.truck_id if route.assigned_truck else "","|".join(str(p.id) for p in route.packages),
                                " -> ".join(time.strftime("%Y-%m-%d-%H:%M") for time in route.arrival_times)])

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
        """
        Creates and registers a package for delivery.

    Args:
        customer_name (str): The name of the customer requesting the package.
        customer_phone (str): The customer's phone number.
        start_loc (str): The starting location of the package.
        end_loc (str): The destination location of the package.
        weight (int): The package weight in kilograms.

    Returns:
        Package: An instance of the Package class representing the newly created package.
        """
        package = Package(customer_name, customer_phone, start_loc, end_loc, weight)
        self._packages.append(package)
        return package
         
    def find_package_by_id(self,package_id):
        """
        Finds package by provided ID Number.

    Args:
        package_id (int): The ID Number of the registered package.

    Returns:
        Package: An instance of the Package class representing the package, associated with the provided ID.

    Raises:
        ValueError: If a package, associated with such an ID Number, does not exist.

        """
        for package in self.packages:
            if package.id == package_id:
                return package
        raise ValueError(f"Package with ID: {package_id} does not exist.")
                    
    def create_route(self, departure_time, start_loc, *next_loc):
        """
        Creates and registers a route.

    Args:
        departure_time (datime): formatted datetime string (e.g., "2025-02-11T14:30").
        start_loc (str): starting location.
        *next_loc (str): the next N-locations of the route, including the final destination.

    Returns:
        Route: An instance of the Route class representing the newly created route.

    Raises:
        ValueError: If the locations are invalid.

        """
        all_locations = [start_loc] + list(next_loc)
        invalid_locations = [loc for loc in all_locations if loc not in Locations.locations]
        if invalid_locations:
            raise ValueError(f"Invalid locations: {', '.join(invalid_locations)}")
        route = Route(departure_time, start_loc, *next_loc)
        self._routes.append(route)
        return route
    
    def find_route_by_id(self,route_id):
        """
        Looks for a route by ID number.

    Args:
        route_id (int): designated ID number of a route.

    Returns:
        route: An instance of the Route class associated with the designated ID number.

    Raises:
        ValueError: If a route associated with the designated ID does not exist.

        """
        for route in self.routes:
            if route.id == route_id:
                return route
        raise ValueError(f"Route with id {route_id} does not exist.")
    

    def create_employee(self, username, firstname, lastname, password, user_role):
        """
        Creates and registers an employee.

    Args:
        username (str): username for logging the employee.
        firstname (str): first name of the employee.
        lastname (str): last name of the employee.
        password (str): password for logging the employee.
        user_role (str): (Optional) if the employee is a manager.

    Returns:
        Route: An instance of the Employee class representing the newly created employee.

    Raises:
        ValueError: If an employee with the same username already exists.

        """
        if len([u for u in self._employees if u.username == username]) > 0:
            raise ValueError(
                f'Employee username: {username} already exist.')
        employee = Employee(username, firstname, lastname, password, user_role)
        self._employees.append(employee)
        return employee
    
    def find_employee_by_username(self, username: str):
        """
        Looks for employee by username.

    Args:
        username (str): username of the employee.

    Returns:
        (str): A string containing the employee username.

    Raises:
        ValueError: If an employee with the username does not exist.

        """
        filtered = [user for user in self._employees if user.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}!')
        return filtered[0]
    
    def login(self, employee: Employee):
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None
        
    def check_truck_has_enough_range_and_is_available(self, total_distance):
        """
        Finds an available truck that has enough range for the given distance.

    Args:
        total_distance (float): The required distance the truck must be able to travel.

    Returns:
        Truck: A suitable truck with sufficient range that is available.

    Raises:
        ValueError: If no truck is available with the required range.
        """
        suitable_trucks = [truck for truck in self.trucks if truck.available and truck.max_range >= total_distance]
        if not suitable_trucks:
            raise ValueError(f"Truck with range {total_distance}km does not exist or not available.")
        return suitable_trucks[0]
    
    def view_routes_in_progress(self):
        """
        Retrieves a list of active routes currently in progress.

    Checks all routes to determine if their departure time has passed but they have not yet arrived at their final destination.
    Includes information about the assigned truck, packages, and route status.

    Returns:
        str: A formatted string listing all active routes with details.
             If no routes are in progress, returns "No routes currently in progress."
        """
        self.update_package_and_truck_status_when_route_is_finished()
        current_time = datetime.now()
        result = "\nRoutes in progress:\n"
        found_in_progress = False
        for route in self.routes:
            if route.departure_time <= current_time < route.arrival_times[-1]:
                found_in_progress = True
                if route.assigned_truck:
                    truck_info = route.assigned_truck.truck_id
                else:
                    truck_info = "No truck assigned to route."
                if route.packages:
                    asgn_packages = " - ".join(f"ID: {package.id} {package.status}" for package in route.packages)
                    weight = sum(int(package.weight) for package in route.packages)
                else:
                    asgn_packages = "No packages assigned"
                    weight = 0
                result += f"Route {route.id}: {' -> '.join(route.locations)}\n"
                result += f"Truck: {truck_info}\n"
                result += f"Assigned packages: {'-'.join(asgn_packages)}\n"
                result += f"Total weight: {weight}\n"
                result += f"Departure time: {route.departure_time}\n"
                result += f"Last stop: {route.current_stop(current_time)}\n"
                result += f"Next stop: {route.next_stop(current_time)}\n"
                result += "\n"
                
        if not found_in_progress:
            return "No routes in progress!"
        return result
    
    def view_unassigned_packages(self):
        """
    Retrieves a list of packages that are not assigned to any route.

    Iterates through all packages and checks if they are assigned to a route.
    If a package is not found in any route, it is considered unassigned.

    Returns:
        str: A formatted string listing unassigned packages and their locations.
             Returns "No unassigned packages" if all packages are assigned.
    """
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
        """
    Retrieves the status of all trucks in the system.

    Updates truck and package statuses, then generates a report of all trucks, 
    showing their assigned routes and availability.

    Returns:
        str: A formatted string listing each truck, its capacity, range, 
        and current availability. If no trucks are available, returns 
        "No trucks available."
        """
        self.update_package_and_truck_status_when_route_is_finished()
        has_available_truck = False
        result = "\nTrucks:\n"
        
        for truck in self.trucks:
            assigned_route = None
            available_time = "Available\n"
            for route in self.routes:
                if route.assigned_truck == truck:
                    assigned_route = route
                    break
                
            result += f"\nTruck {truck.truck_id}: {truck.brand}, Capacity: {truck.capacity}kg, Max Range: {truck.max_range}km.\n"
            if assigned_route:
                current_time = datetime.now()
                if assigned_route.departure_time > current_time:
                    available_time = assigned_route.departure_time.strftime("%Y-%m-%d-%H:%M")
                    result += f"Assigned to Route {assigned_route.id} - Will be available until {available_time}.\n"
                else:
                    available_time = assigned_route.arrival_times[-1].strftime("%Y-%m-%d-%H:%M")
                    result += f"Assigned to Route {assigned_route.id} - Will be available after {available_time}.\n"
            else:
                has_available_truck = True
                result += "Available\n"       
        if not has_available_truck:
            return "No trucks available."
        
        return result
    
    
