from commands.base_command import BaseCommand
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 18bdbd2 (created view packages)
from core.application_data import Application_data
class ViewPackages(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
        
    def execute(self, params):
        super().execute(params)
        
<<<<<<< HEAD
<<<<<<< HEAD
        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")
        
        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can view packages!")
=======
        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can view routes!")
>>>>>>> 18bdbd2 (created view packages)
=======
        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")
        
        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can view packages!")
>>>>>>> 1cea707 (Working code)
        
        return self._app_data.view_unassigned_packages()
    
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
<<<<<<< HEAD
    
=======
class ViewPackages(BaseCommand):
    pass
>>>>>>> 3588a2d (Created assigntrucktoroute added all files needed for the project added some commands in appdata and fixed output if invalid city is entered.)
=======
    
>>>>>>> 18bdbd2 (created view packages)
