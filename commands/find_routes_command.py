from commands.base_command import BaseCommand
from datetime import datetime
from models.locations import Locations


class FindRoutes(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 2:
            raise ValueError("Invalid input!Expected: start location and end location.")

        start_location, end_location = params
        current_time = datetime.now()

        if start_location not in Locations.locations:
            return f"Invalid location: {start_location} does not exist."
        if end_location not in Locations.locations:
            return f"Invalid location: {end_location} does not exist."

        matching_routes = [
            route for route in self._app_data.routes
            if start_location in route.locations
            and end_location in route.locations
            and route.locations.index(start_location) < route.locations.index(end_location)
            and route.departure_time > current_time
        ]

        if not matching_routes:
            return f"No routes found from {start_location} to {end_location}."

        result = "\n".join(str(route) for route in matching_routes)
        return f"Routes from {start_location} to {end_location}:\n{result}"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2
