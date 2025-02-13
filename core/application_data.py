from models.employee import Employee
from models.package import Package
from models.route import Route
from models.truck_car_park import TruckCarPark

class ApplicationData:
    def __init__(self):
        self._employees = []
        self._packages = []
        self._routes = []
        self._logged_employee = None

    @property
    def employees(self):
        return tuple(self._employees)
    
    @property
    def routes(self):
        return tuple(self._routes)
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    def create_package(self, customer_name, customer_phone, start_loc, end_loc, weight):
        package = Package(customer_name, customer_phone, start_loc, end_loc, weight)
        self._packages.append(package)
        return package
    
    # def assign_package_to_truck(self, package_id, truck_id):
    #     for pack in self._packages:
    #         if pack.id != package_id:
    #             raise ValueError(f"Package with ID #{package_id} does not exist.")
    #     if truck_id not in TruckCarPark.list_all_free_trucks():
    #         raise ValueError(f'Truck with ID #{truck_id} is not available.')
    
    def create_route(self, departure_time, start_loc, *next_loc):
        route = Route(departure_time, start_loc, *next_loc)
        self._routes.append(route)
        return route
    
    def search_route(self, start_loc, end_loc):
        final_routes = []
        routes_contain = [route for route in self._routes if start_loc in route.all_locations and end_loc in route.all_locations]
        for route in routes_contain:
            if start_loc != route.all_locations[0]:
                raise ValueError("Route doesn't exist.")
            final_routes.append(route)
        return final_routes


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