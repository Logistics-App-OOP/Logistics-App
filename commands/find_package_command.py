from commands.base_command import BaseCommand
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1cea707 (Working code)
from core.application_data import Application_data
class FindPackage(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
    
    
    def execute(self, params):
        super().execute(params)
        
        if len(params) != 1:
            raise ValueError("Invalid input!Expected: Package ID.")
        
<<<<<<< HEAD
        self._app_data.update_package_and_truck_status_when_route_is_finished()
=======
        self._app_data.update_package_status_to_delivered()
>>>>>>> 1cea707 (Working code)
        
        package_id = int(params[0])
        
        package = self._app_data.find_package_by_id(package_id)
        
        return (
            f"Package ID: {package_id}\n"
            f"Customer name: {package.customer_name}\n"
            f"Phone: {package.customer_phone}\n"
            f"From: {package.start_loc}\n"
            f"To: {package.end_loc}\n"
            f"Weight: {package.weight} kg\n"
            f"Status: {package.status}\n"
        )
        
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
        
        
        
        
        
        
<<<<<<< HEAD
        
=======
class FindPackage(BaseCommand):
    pass
>>>>>>> 3588a2d (Created assigntrucktoroute added all files needed for the project added some commands in appdata and fixed output if invalid city is entered.)
=======
        
>>>>>>> 1cea707 (Working code)
