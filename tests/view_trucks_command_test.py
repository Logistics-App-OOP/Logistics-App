import unittest
from datetime import datetime, timedelta
from commands.view_trucks_command import ViewTrucks
from core.application_data import Application_data
from models.locations import Locations

class ViewTrucksCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.app_data.login(self.app_data.employees[0])
        self.command = ViewTrucks(self.app_data)
        self.app_data._routes = []

    def test_should_raise_error_if_not_logged_in(self):
        self.app_data.logout()
        with self.assertRaises(ValueError) as context:
            self.command.execute([])
        self.assertEqual(str(context.exception), "You are not logged in! Please login first!")

    def test_should_raise_error_if_invalid_input_provided(self):
        with self.assertRaises(ValueError) as context:
            self.command.execute(["unexpected"])
        self.assertEqual(str(context.exception), "Invalid input! No input expected.")

    def test_should_raise_error_if_logged_in_employee_is_not_manager(self):
        non_manager = self.app_data.create_employee("employee1", "Employee", "User", "password1", "Normal")
        self.app_data.login(non_manager)
        with self.assertRaises(ValueError) as context:
            self.command.execute([])
        self.assertEqual(str(context.exception), "You are not manager,only Managers can view trucks!")

    def test_should_return_trucks_list_when_trucks_available(self):
        result = self.command.execute([])
        self.assertIn("\nTrucks:\n", result)
        self.assertIn("Available", result)

    def test_should_return_no_trucks_available_when_none_exist(self):
        self.app_data._trucks = []
        result = self.command.execute([])
        self.assertEqual(result, "No trucks available.")

    def test_should_show_assigned_route_info(self):
        now = datetime.now()
        departure_time = now + timedelta(hours=1)
        valid_locations = list(Locations.locations)
        start_loc = valid_locations[0]
        next_loc = valid_locations[1] if len(valid_locations) > 1 else valid_locations[0]
        route = self.app_data.create_route(departure_time, start_loc, next_loc)
        truck = self.app_data.trucks[0]
        route.assign_truck(truck)
        result = self.command.execute([])
        self.assertIn(f"Truck {truck.truck_id}:", result)
        self.assertIn(f"Assigned to Route {route.id}", result)
        self.assertIn("Available", result)
