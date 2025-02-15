<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 55ed752 (Rebased from main)
from commands.base_command import BaseCommand
<<<<<<< HEAD
<<<<<<< HEAD
from core.application_data import Application_data

class CreatePackage(BaseCommand):
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
=======
from commands.validate_params import validate_params_count
=======
from commands.base_command import BaseCommand
from core.application_data import Application_data

class CreatePackage(BaseCommand):
<<<<<<< HEAD
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)
>>>>>>> 68cae1d (Created truck editted app_data, route,package)
=======
    def __init__(self, app_data: Application_data):
        self._app_data = app_data
>>>>>>> 7706c1c (Created CreateRoute)

    def execute(self, params):
        super().execute(params)
        
        if len(params) != 5:
            raise ValueError("Invalid input!Expected: Customer name, customer phone number, start location, End location, package weight")
<<<<<<< HEAD

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
=======
>>>>>>> 1cea707 (Working code)

        customer_name, customer_phone, start_loc, end_loc, weight = params

<<<<<<< HEAD
<<<<<<< HEAD
        package= self._app_data.create_package(customer_name, customer_phone, start_loc, end_loc, weight)


        return f"{package.customer_name}'s package registered successfully with ID: {package.id}!"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
=======
>>>>>>> 5657f45 (Rebased from main)
=======
from commands.validate_params import validate_params_count
>>>>>>> 6cabb68 (update branch)
<<<<<<< HEAD
>>>>>>> e431c9e (update branch)
=======
=======
        package = self._app_data.create_package(
            customer_name, customer_phone, start_loc, end_loc, weight)
=======
        package= self._app_data.create_package(customer_name, customer_phone, start_loc, end_loc, weight)
>>>>>>> 7706c1c (Created CreateRoute)


        return f"{package.customer_name}'s package registered successfully!"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
>>>>>>> 68cae1d (Created truck editted app_data, route,package)
<<<<<<< HEAD
>>>>>>> e6a5d05 (Created truck editted app_data, route,package)
=======
=======
>>>>>>> 55ed752 (Rebased from main)
>>>>>>> 5657f45 (Rebased from main)
