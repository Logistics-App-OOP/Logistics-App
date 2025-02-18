from tomlkit import date
from models.package import Package
from commands.base_command import BaseCommand
from core.application_data import Application_data
from models.route import Route
from datetime import datetime
class AssignPackageToRoute(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
        
    def execute(self, params):
        super().execute(params)
        
        if len(params) != 2:
            raise ValueError("Invalid input! Expected input: package id, route id.")
        
        current_time = datetime.now()
        package_id = int(params[0])
        route_id = int(params[1])
        
        package: Package = self._app_data.find_package_by_id(package_id)
        route: Route = self._app_data.find_route_by_id(route_id)
        
        if route.assigned_truck is None:
            return f"Package {package_id} cannot be assigned to Route {route_id}.\nNo truck assigned to Route {route_id}."
        
        if package.start_loc not in route.locations or package.end_loc not in route.locations:
            return f"Package {package_id} cannot be assigned to Route {route_id} the locations does not match."
        if route.locations.index(package.start_loc) >= route.locations.index(package.end_loc):
            return f"Package {package_id} cannot be assigned to Route {route_id}.\nDirection of the route does not match {package.start_loc} -> {package.end_loc}."
        
        if int(route.assigned_truck.capacity) < int(package.weight):
            return f"Package {package_id} cannot be assigned to Route {route_id}.\nTruck {route.assigned_truck.truck_id} dont have enough storage {route.assigned_truck.capacity}kg < {package.weight}kg."
                
        if package.status != "Created":
            raise ValueError(f"Error! Package {package.id} already assigned and cannot be assigned twice.")
        route.assign_package(package)
        if not route.departure_time > current_time:
            package.update_status() 
        route.assigned_truck.capacity -= int(package.weight)
        
        return f"Package {package_id} assigned to Route {route_id}.\nRemaining truck capacity {route.assigned_truck.capacity}kg."
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2
