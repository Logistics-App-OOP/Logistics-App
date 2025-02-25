import unittest
from unittest.mock import Mock
from datetime import datetime

from commands.assign_package_to_route_comand import AssignPackageToRoute
from core.application_data import Application_data
from models.route import Route
from models.package import Package
from models.truck import Truck

class TestAssignPackageToRoute(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock()

        self.route_1 = Route(departure_time=datetime(2025, 5, 10, 10, 0), start_loc="Sydney")
        self.package_1 = Package(customer_name='LyuboP',customer_phone='0404040404',  weight=10, start_loc="Sydney", end_loc="Melbourne")
        self.package_2 = Package(customer_name='LyuboEG',customer_phone='0404040414',  weight=55, start_loc="Sydney", end_loc="Perth")

        self.truck_1 = Truck(truck_id=1, brand="TruckCo", capacity=20, max_range=1000)
        self.route_1.assigned_truck = self.truck_1

        self.app_data.find_package_by_id.return_value = self.package_1
        self.app_data.find_route_by_id.return_value = self.route_1

        self.command = AssignPackageToRoute(self.app_data)
        self.command._app_data = self.app_data

    def test_package_already_assigned(self):
        self.package_1.status = "Created"
        params = [str(self.package_1.id)]

        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_no_truck_assigned_to_route(self):
        self.route_1.assigned_truck = None
        params = [str(self.package_1.id), str(self.route_1.id)]

        result = self.command.execute(params)
        expected_result = f"Package {self.package_1.id} cannot be assigned to Route {self.route_1.id}.\nNo truck assigned to Route {self.route_1.id}."
        self.assertEqual(result, expected_result)

    def test_invalid_route_id(self):
        params = ['a', '1']
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_invalid_params_count(self):
        params = ["123", "456", "789"]
        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_no_route_found(self):
        self.app_data.find_route_by_id.return_value = None
        params = [str(self.package_1.id), '']

        with self.assertRaises(ValueError):
            self.command.execute(params)

    def test_missing_param(self):
        params = [str(self.package_1.id)]

        with self.assertRaises(ValueError):
            self.command.execute(params)

