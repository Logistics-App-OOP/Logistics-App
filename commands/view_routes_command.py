from commands.base_command import BaseCommand
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ce17e5b (created viewroutes and updated app_data and route)
from core.application_data import Application_data
class ViewRoutes(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
    
    def execute(self, params):
        super().execute(params)
        
<<<<<<< HEAD
        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")
        
=======
>>>>>>> ce17e5b (created viewroutes and updated app_data and route)
        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can view routes!")    
        
        return self._app_data.view_routes_in_progress()
        
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
<<<<<<< HEAD
        return 0
=======
class ViewRoutes(BaseCommand):
    pass
>>>>>>> 3588a2d (Created assigntrucktoroute added all files needed for the project added some commands in appdata and fixed output if invalid city is entered.)
=======
        return 0
>>>>>>> ce17e5b (created viewroutes and updated app_data and route)
