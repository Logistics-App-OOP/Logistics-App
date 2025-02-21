import unittest
from unittest.mock import Mock
from datetime import datetime
from commands.create_route_command import CreateRouteCommand
from models.route import Route


class TestCreateRouteCommand(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock()

        self.route = Route(datetime.strptime("2026-02-11-14:30", "%Y-%m-%d-%H:%M"), 'Sydney', 'Perth')

        self.app_data.create_route.return_value = self.route

        self.command = CreateRouteCommand(self.app_data)
        self.command._app_data = self.app_data

    def test_create_route_successful(self):
        params = ["2026-02-11-14:30", "New York", "Chicago", "Los Angeles"]
        result = self.command.execute(params)

        expected_result = str(self.route)
        self.assertEqual(result, expected_result)

    def test_invalid_date_format(self):
        params = ["2026/02/11/14:30", "New York", "Chicago", "Los Angeles"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_invalid_params_count(self):
        params = ["2026-02-11-14:30", "New York"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_create_route_internal_error(self):
        self.app_data.create_route.side_effect = Exception("Internal error occurred")
        params = ["2026-02-11-14:30", "New York", "Chicago", "Los Angeles"]

        with self.assertRaises(Exception):
            self.command.execute(params)

    def test_missing_start_location(self):
        params = ["2026-02-11-14:30", "Los Angeles"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_create_route_empty_next_locations(self):
        params = ["2026-02-11-14:30", "New York", []]
        result = self.command.execute(params)
        expected_result = str(self.route)
        self.assertEqual(result, expected_result)



