from datetime import datetime
from models.route import Route
from commands.base_command import BaseCommand
from core.application_data import Application_data

class CreateRouteCommand(BaseCommand):
    def __init__(self, app_data: Application_data):
        super().__init__(app_data)
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)

        if len(params) < 2:
            raise ValueError("Invalid input! Expected: departure_time start_location [next_locations...]")

        departure_time_str,start_loc,*next_locations = params
       
        try:
            departure_time = datetime.strptime(departure_time_str, "%Y-%m-%dT%H:%M")
        except ValueError:
            raise ValueError("Invalid date format! Use YYYY-MM-DDTHH:MM (e.g., 2025-02-11T14:30)")

        route = self._app_data.create_route(departure_time, start_loc, *next_locations)
        
        return str(route)
    
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 3