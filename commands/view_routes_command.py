from commands.base_command import BaseCommand


class ViewRoutes(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")

        if not self._app_data.logged_in_employee.is_manager():
            raise ValueError("You are not manager,only Managers can view routes!")

        return self._app_data.view_routes_in_progress()

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
