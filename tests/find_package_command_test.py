import unittest
from commands.find_package_command import FindPackage
from core.application_data import Application_data

class FindPackage_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.command = FindPackage(self.app_data)
        self.employee = self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
        self.app_data.login(self.employee)
        self.test_package = self.app_data.create_package("Uasim", "0404040404", "Sydney", "Melbourne", 45)

    def test_should_return_package_details(self):
        package_id = self.test_package.id
        result = self.command.execute([package_id])

        self.assertIn(f"Package ID: {package_id}", result)
        self.assertIn("Customer name: Uasim", result)
        self.assertIn("Phone: 0404040404", result)
        self.assertIn("From: Sydney", result)
        self.assertIn("To: Melbourne", result)
        self.assertIn("Weight: 45 kg", result)
        self.assertIn("Status: Created", result)

    def test_should_raise_error_if_no_package_id(self):
        with self.assertRaises(ValueError):
            self.command.execute([])

    def test_should_raise_error_if_too_many_params(self):
        with self.assertRaises(ValueError):
            self.command.execute([1, 2])

    def test_should_raise_error_if_package_not_found(self):
        with self.assertRaises(ValueError):
            self.command.execute([99999])