import unittest
from unittest.mock import Mock
from models.package import Package
from commands.create_package_command import CreatePackage
from datetime import datetime


class TestCreatePackage(unittest.TestCase):

    def setUp(self):
        self.app_data = Mock()

        self.package = Package(customer_name="John Doe", customer_phone="0411223344", start_loc="Sydney",
                               end_loc="Melbourne", weight=45)

        self.app_data.create_package.return_value = self.package

        self.command = CreatePackage
        self.command._app_data = self.app_data

    def test_create_package_successful(self):
        params = ["John Doe", "123-456-7890", "New York", "Los Angeles", 5]
        result = self.command.execute(CreatePackage(self.app_data), params)

        expected_result = f"{self.package.customer_name}'s package registered successfully with ID: {self.package.id}!"
        self.assertEqual(result, expected_result)

    def test_invalid_params_count(self):
        params = ["John Doe", "123-456-7890", "New York", "Los Angeles"]  # Missing weight
        with self.assertRaises(ValueError):
            self.command.execute(CreatePackage(self.app_data), params)

    def test_create_package_internal_error(self):
        self.app_data.create_package.side_effect = Exception("Internal error occurred")
        params = ["John Doe", "123-456-7890", "New York", "Los Angeles", "5.0"]

        with self.assertRaises(Exception):
            self.command.execute(CreatePackage(self.app_data), params)

    def test_create_package_missing_data(self):
        params = ["", "123-456-7890", "New York", "Los Angeles", "5.0"]
        result = self.command.execute(CreatePackage(self.app_data), params)
        expected_result = "Invalid input!Expected: Customer name, customer phone number, start location, End location, package weight"
        self.assertEqual(expected_result, expected_result)

    def test_create_package_missing_customer_name(self):
        params = ["123-456-7890", "New York", "Los Angeles", "5.0"]
        with self.assertRaises(ValueError):
            self.command.execute(CreatePackage(self.app_data), params)



