from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from datetime import datetime, timedelta

class CreateRoute(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        departure_date_str, start_loc, *next_loc = params

        try:
            departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d")
        except ValueError:
            return "Invalid departure date format. Please use 'YYYY-MM-DD' format."

        departure_time = datetime.combine(departure_date, datetime.min.time()) + timedelta(hours=6)

        route = self._app_data.create_route(departure_time, start_loc, *next_loc)

        return f'Route {str(route)} created successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 3
    
    def _requires_manager(self) -> bool:
        return False
    
    def _requires_supervisor(self) -> bool:
        return False
