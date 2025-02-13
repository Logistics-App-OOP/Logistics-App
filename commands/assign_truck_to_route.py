from commands.base_command import BaseCommand
from core.application_data import Application_data

class CreatePackage(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
        
    def execute(self, params):
        super().execute(params)
        
        #params
        
        
        
        
        
        
        
        
    # def _requires_login(self) -> bool:
    #     return True

    # def _expected_params_count(self) -> int:
    #     return 5
