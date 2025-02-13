from commands.base_command import BaseCommand
from core.application_data import Application_data


class RegisterEmployeeCommand(BaseCommand):
    def __init__(self, app_data: Application_data):
<<<<<<< HEAD
=======
        super().__init__(app_data)
>>>>>>> 4c07a03 (Created CreateRoute)
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)
        self._throw_if_employee_logged_in()
<<<<<<< HEAD
        
        if len(params) != 5:
            raise ValueError("Invalid input!Expected: username,first name, last name, password, role.")
        
=======
>>>>>>> 4c07a03 (Created CreateRoute)
        username, firstname, lastname, password, user_role = params
        user = self._app_data.create_employee(
            username, firstname, lastname, password, user_role)
        return f'Employee {user.username} registered successfully!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 5
    