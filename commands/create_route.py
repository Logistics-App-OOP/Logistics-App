from commands.base_command import BaseCommand
from core.application_data import ApplicationData

class CreateRoute(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        start_loc, *next_loc = params

        route = self._app_data.create_route(
            start_loc, *next_loc)

        return f'Route {str(route)} created successfully!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2
