<<<<<<< HEAD
from commands.validate_params import validate_params_count
=======
from commands.base_command import BaseCommand
from core.application_data import Application_data

class CreatePackage(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)

        customer_name, customer_phone, start_loc, end_loc, weight = params

        package= self._app_data.create_package(customer_name, customer_phone, start_loc, end_loc, weight)


        return f"{package.customer_name}'s package registered successfully!"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
