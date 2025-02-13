from commands.base_command import BaseCommand
<<<<<<< HEAD
<<<<<<< HEAD
from core.application_data import Application_data

class CreatePackage(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data

    def execute(self, params):
        super().execute(params)
        
        if len(params) != 5:
            raise ValueError("Invalid input!Expected: Customer name, customer phone number, start location, End location, package weight")

        customer_name, customer_phone, start_loc, end_loc, weight = params

        package= self._app_data.create_package(customer_name, customer_phone, start_loc, end_loc, weight)


        return f"{package.customer_name}'s package registered successfully with ID: {package.id}!"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
=======
from core.application_data import ApplicationData
=======
from core.application_data import Application_data
>>>>>>> 4c07a03 (Created CreateRoute)

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
