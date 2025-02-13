from commands.base_command import BaseCommand
from core.application_data import ApplicationData

class CreatePackage(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        customer_name, customer_phone, start_loc, end_loc, weight = params

        package = self._app_data.create_package(
            customer_name, customer_phone, start_loc, end_loc, weight)
        
        # routes = self._app_data.search_route(start_loc, end_loc)

        # formatted_routes = "\n".join(str(route) for route in routes)

        return f'Package (ID: #{package.id}) by {package.customer_name} registered successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
    
    def _requires_manager(self) -> bool:
        return False
    
    def _requires_supervisor(self) -> bool:
        return False

