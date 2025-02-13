from datetime import datetime
<<<<<<< HEAD
<<<<<<< HEAD
=======
from re import A
>>>>>>> 4c07a03 (Created CreateRoute)
=======
>>>>>>> 9b3c1fa (created find routes and create routes)
from models.route import Route
from commands.base_command import BaseCommand
from core.application_data import Application_data

class CreateRouteCommand(BaseCommand):
    def __init__(self, app_data: Application_data):
<<<<<<< HEAD
=======
        super().__init__(app_data)
>>>>>>> 4c07a03 (Created CreateRoute)
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)

<<<<<<< HEAD
        if len(params) < 3:
=======
        if len(params) < 2:
>>>>>>> 4c07a03 (Created CreateRoute)
            raise ValueError("Invalid input! Expected: departure_time start_location [next_locations...]")

        departure_time_str,start_loc,*next_locations = params
       
        try:
            departure_time = datetime.strptime(departure_time_str, "%Y-%m-%dT%H:%M")
        except ValueError:
            raise ValueError("Invalid date format! Use YYYY-MM-DDTHH:MM (e.g., 2025-02-11T14:30)")

        route = self._app_data.create_route(departure_time, start_loc, *next_locations)
<<<<<<< HEAD
<<<<<<< HEAD
        
        return str(route)
=======

        full_route = " -> ".join(route.locations)  
        return f"Route {route.id} created successfully: {full_route} with departure at {route.departure_time.strftime('%b %d %H:%M')}!"
>>>>>>> 4c07a03 (Created CreateRoute)
=======
        
        return str(route)
>>>>>>> 9b3c1fa (created find routes and create routes)
    
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 3