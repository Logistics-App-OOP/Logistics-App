from commands.base_command import BaseCommand
from core.application_data import Application_data


class LogoutCommand(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)
<<<<<<< HEAD
<<<<<<< HEAD
        
        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")
=======
>>>>>>> 4c07a03 (Created CreateRoute)
=======
        
        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")
>>>>>>> 1cea707 (Working code)

        self._app_data.logout()

        return 'You logged out!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0