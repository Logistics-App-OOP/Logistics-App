# from commands.base_command import BaseCommand
# from core.application_data import ApplicationData

# class AssignPackageToTruck(BaseCommand):
#     def __init__(self, app_data: ApplicationData):
#         super().__init__(app_data)

#     def execute(self, params):
#         super().execute(params)

#         package_id, truck_id = params

#         self._app_data.assign_package_to_truck(package_id, truck_id)

#         return f'Package (ID: #{package_id}) has been assigned to Truck (ID: #{truck_id}).'

#     def _requires_login(self) -> bool:
#         return False

#     def _expected_params_count(self) -> int:
#         return 2