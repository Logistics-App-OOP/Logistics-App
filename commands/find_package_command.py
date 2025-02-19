from commands.base_command import BaseCommand
from core.application_data import Application_data


class FindPackage(BaseCommand):

    def execute(self, params):
        super().execute(params)

        if len(params) != 1:
            raise ValueError("Invalid input!Expected: Package ID.")

        self._app_data.update_package_and_truck_status_when_route_is_finished()

        package_id = int(params[0])

        package = self._app_data.find_package_by_id(package_id)

        return (
            f"Package ID: {package_id}\n"
            f"Customer name: {package.customer_name}\n"
            f"Phone: {package.customer_phone}\n"
            f"From: {package.start_loc}\n"
            f"To: {package.end_loc}\n"
            f"Weight: {package.weight} kg\n"
            f"Status: {package.status}\n"
        )

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
