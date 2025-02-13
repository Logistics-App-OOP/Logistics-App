from models.truck import Truck
from models.employee import Employee
from models.package import Package
from models.route import Route
from models.employee import Employee

class Application_data:
    
    def __init__(self):
        self._employees: list[Employee] = []
        self._packages: list[Package] = []
        self._routes: list[Route] = []
        self._trucks = []
        self._adding_trucks()
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
                f'Employee username: {username} already exist.')
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
        
    
