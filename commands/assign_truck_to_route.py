from commands.base_command import BaseCommand
from core.application_data import Application_data
from models.route import Route


class AssignTruckToRoute(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 1:
            raise ValueError("Invalid input! Expected input: route id.")

        route_id = int(params[0])

        route: Route = self._app_data.find_route_by_id(route_id)

        if route.assigned_truck:
            return f"Route {route_id} has already truck:{route.assigned_truck.truck_id} assigned."

        route_distance = route.total_distance()

        try:
            truck = self._app_data.check_truck_has_enough_range_and_is_available(route_distance)
        except ValueError as e:
            return str(e)

        route.assign_truck(truck)
        truck.assign_to_route(route)
        return f"Truck {truck.truck_id} assigned to Route {route_id} with total distance {route_distance}km."

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 1
