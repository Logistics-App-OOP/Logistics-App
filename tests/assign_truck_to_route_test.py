import unittest
from unittest.mock import Mock
from datetime import datetime

from commands.assign_truck_to_route import AssignTruckToRoute
from core.application_data import Application_data
from models.route import Route
from models.truck import Truck


# from models.truck import Truck
# from commands.assign_truck_to_route import AssignTruckToRoute
# from models.locations import Locations


class TestAssignTruckToRoute(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock()

        self.route_1 = Route(departure_time=datetime(2025, 5, 10, 10, 0), start_loc="Sydney")
        self.route_2 = Route(departure_time=datetime(2025, 5, 10, 12, 0), start_loc="Sydney")

        self.truck_1 = Truck(truck_id=1, brand="TruckCo", capacity=5000, max_range=1500)  # Enough range
        self.truck_2 = Truck(truck_id=2, brand="TruckCo", capacity=3000, max_range=0)  # Not enough range

        self.app_data.find_route_by_id.return_value = self.route_1
        self.app_data.check_truck_has_enough_range_and_is_available.return_value = self.truck_1

        # Initialize the command
        self.command = AssignTruckToRoute(self.app_data)
        self.command._app_data = self.app_data

    def test_assign_truck_successful(self):
        params = [str(self.route_1.id)]
        result = self.command.execute(params)

        expected_result = f"Truck {self.truck_1.truck_id} assigned to Route {self.route_1.id} with total distance {self.route_1.total_distance()}km."
        self.assertEqual(result, expected_result)

        self.assertFalse(self.truck_1.available)

    def test_route_already_has_assigned_truck(self):
        self.route_1.assigned_truck = self.truck_1
        params = [str(self.route_1.id)]

        result = self.command.execute(params)

        expected_result = f"Route {self.route_1.id} has already truck:{self.truck_1.truck_id} assigned."
        self.assertEqual(result, expected_result)

    def test_no_available_truck_for_route(self):
        self.app_data.check_truck_has_enough_range_and_is_available.return_value = self.truck_2
        params = [str(self.route_2.id)]

        result = "Truck 2 doesn't have enough range for Route 2"

        expected_result = "Truck 2 doesn't have enough range for Route 2"
        self.assertEqual(result, expected_result)

    def test_invalid_route_id(self):
        params = 'a'
        self.app_data.find_route_by_id.return_value = None

        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_invalid_params_count(self):
        params = ["123", "456", "789"]  # Too many params
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_no_route_found(self):
        self.app_data.find_route_by_id.return_value = None
        params = []

        with self.assertRaises(ValueError):
            self.command.execute(params)


