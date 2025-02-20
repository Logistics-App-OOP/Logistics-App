from commands.base_command import BaseCommand


class RegisterEmployeeCommand(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 5:
            raise ValueError("Invalid input!Expected: username,first name, last name, password, role.")
        
        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can register employees!")

        username, firstname, lastname, password, user_role = params
        user = self._app_data.create_employee(
            username, firstname, lastname, password, user_role)
        return f'Employee {user.username} registered successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
