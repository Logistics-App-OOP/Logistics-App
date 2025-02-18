import unittest
from commands.find_routes_command import FindRoutes
from core.application_data import Application_data
from datetime import datetime

class FindRoutes_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.command = FindRoutes(self.app_data)

        self.employee = self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
        self.app_data.login(self.employee)

    def test_should_return_error_if_start_location_invalid(self):
        result = self.command.execute(["InvalidCity", "Brisbane"])
        self.assertEqual(result, "Invalid location: InvalidCity does not exist.")
        
    def test_should_raise_error_if_no_locations_provided(self):
        with self.assertRaises(ValueError):
            self.command.execute([])

    def test_should_raise_error_if_too_many_locations_provided(self):
        with self.assertRaises(ValueError):
            self.command.execute(["Sydney", "Brisbane", "Darwin"])