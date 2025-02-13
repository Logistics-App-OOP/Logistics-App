# from commands.base_command import BaseCommand
# from core.application_data import ApplicationData

# class AssignTruckToRoute(BaseCommand):
#     def __init__(self, app_data: ApplicationData):
#         super().__init__(app_data)

#     def execute(self, params):
#         super().execute(params)

#         truck_id, route_id = params

#         self._app_data.assign_truck_to_route(truck_id, route_id)

#         return f'Truck (ID: #{truck_id}) has been assigned to Route (ID: #{route_id}).'

#     def _requires_login(self) -> bool:
#         return False

#     def _expected_params_count(self) -> int:
#         return 2
