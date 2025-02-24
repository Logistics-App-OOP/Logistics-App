import unittest
from datetime import datetime, timedelta
from commands.view_routes_command import ViewRoutes
from core.application_data import Application_data
from models.locations import Locations

class ViewRoutesCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.app_data.login(self.app_data.employees[0])
        self.command = ViewRoutes(self.app_data)
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
        self.assertEqual(str(context.exception), "You are not manager,only Managers can view routes!")

    def test_should_return_no_routes_available(self):
        result = self.command.execute([])
        self.assertEqual(result, "No routes available!")

    def test_should_return_routes_in_progress(self):
        now = datetime.now()
        departure_time = now - timedelta(hours=1)
        valid_locations = list(Locations.locations)
        if "Sydney" in valid_locations and "Melbourne" in valid_locations:
            start_loc = "Sydney"
            next_loc = "Melbourne"
        else:
            start_loc = valid_locations[0]
            next_loc = valid_locations[1] if len(valid_locations) > 1 else valid_locations[0]
        route = self.app_data.create_route(departure_time, start_loc, next_loc)
        result = self.command.execute([])
        self.assertIn("Routes in progress:", result)
        self.assertIn(f"Route {route.id}:", result)
        self.assertIn("No truck assigned to route.", result)
        self.assertIn("No packages assigned", result)