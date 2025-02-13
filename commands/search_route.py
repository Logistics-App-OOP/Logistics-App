from commands.base_command import BaseCommand
from core.application_data import ApplicationData

class SearchRoute(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        start_loc, end_loc = params

        routes = self._app_data.search_route(start_loc, end_loc)

        formatted_routes = "\n".join(str(route) for route in routes)

        return f"These routes have been found:\n{formatted_routes}"


    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2
    
    def _requires_manager(self) -> bool:
        return False
    
    def _requires_supervisor(self) -> bool:
        return False