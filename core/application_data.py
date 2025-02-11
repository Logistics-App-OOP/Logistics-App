
from models.package import Package
from models.route import Route
from models.truck import Truck
class ApplicationData:
    def __init__(self):
        
        self._packages:list[Package] = []
        self._routes: list[Route] = []
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
        
        
    @property
    def packages(self):
        return self._packages
    
    @property
    def routes(self):
        return self._routes
    
    @property
    def trucks(self):
        return self._trucks
    
    def add_package(self,package):
        self.packages.append(package)
        
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
