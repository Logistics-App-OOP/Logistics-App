import unittest
from unittest.mock import Mock
from datetime import datetime
from commands.create_route_command import CreateRouteCommand
from models.route import Route


class TestCreateRouteCommand(unittest.TestCase):

    def setUp(self):
        # Create a mock for _app_data
        self.app_data = Mock()

        # Create a mock Route object
        self.route = Route(datetime.strptime("2026-02-11-14:30", "%Y-%m-%d-%H:%M"), 'Sydney', 'Perth')

        # Set up the app data mock to return a route when create_route is called
        self.app_data.create_route.return_value = self.route

        # Initialize the command
        self.command = CreateRouteCommand(self.app_data)
        self.command._app_data = self.app_data

    def test_create_route_successful(self):
        # Test for valid input params
        params = ["2026-02-11-14:30", "New York", "Chicago", "Los Angeles"]
        result = self.command.execute(params)

        expected_result = str(self.route)
        self.assertEqual(result, expected_result)

    def test_invalid_date_format(self):
        # Test for invalid departure_time format
        params = ["2026/02/11/14:30", "New York", "Chicago", "Los Angeles"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_invalid_params_count(self):
        # Test for incorrect number of parameters
        params = ["2026-02-11-14:30", "New York"]  # Missing next locations
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_create_route_internal_error(self):
        # Test when the _app_data create_route fails internally
        self.app_data.create_route.side_effect = Exception("Internal error occurred")
        params = ["2026-02-11-14:30", "New York", "Chicago", "Los Angeles"]

        with self.assertRaises(Exception):
            self.command.execute(params)

    def test_missing_start_location(self):
        # Test for missing start location
        params = ["2026-02-11-14:30", "Los Angeles"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_create_route_empty_next_locations(self):
        # Test for empty next locations
        params = ["2026-02-11-14:30", "New York", []]
        result = self.command.execute(params)
        expected_result = str(self.route)
        self.assertEqual(result, expected_result)



