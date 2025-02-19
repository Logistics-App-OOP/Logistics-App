from commands.base_command import BaseCommand
from core.application_data import Application_data


class LogoutCommand(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 0:
            raise ValueError("Invalid input! No input expected.")

        self._app_data.logout()

        return 'You logged out!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
