from commands.base_command import BaseCommand
from core.application_data import Application_data


class CreatePackage(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 5:
            raise ValueError(
                "Invalid input!Expected: Customer name, customer phone number, start location, End location, package weight")

        customer_name, customer_phone, start_loc, end_loc, weight = params

        package = self._app_data.create_package(customer_name, customer_phone, start_loc, end_loc, weight)

        return f"{package.customer_name}'s package registered successfully with ID: {package.id}!"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5
