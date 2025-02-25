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