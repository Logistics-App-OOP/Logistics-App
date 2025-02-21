from commands.base_command import BaseCommand


class LoginCommand(BaseCommand):

    def execute(self, params):
        super().execute(params)
        self._throw_if_employee_logged_in()

        if len(params) != 2:
            raise ValueError("Invalid input!Expected: username, password.")

        username, password = params
        user = self._app_data.find_employee_by_username(username)
        if user.password != password:
            raise ValueError('Wrong username or password!')
        else:
            self._app_data.login(user)

            return f'Employee {user.username} successfully logged in!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2
