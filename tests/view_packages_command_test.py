import unittest
from commands.view_packages_command import ViewPackages
from core.application_data import Application_data
from models.locations import Locations

class ViewPackagesCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.app_data.login(self.app_data.employees[0])
        self.command = ViewPackages(self.app_data)
        self.app_data._packages = []

    def test_should_raise_error_if_not_logged_in(self):
        self.app_data.logout()
        with self.assertRaises(ValueError) as context:
            self.command.execute([])
        self.assertEqual(str(context.exception), 'You are not logged in! Please login first!')

    def test_should_raise_error_if_invalid_input_provided(self):
        with self.assertRaises(ValueError) as context:
            self.command.execute(['unexpected'])
        self.assertEqual(str(context.exception), "Invalid input! No input expected.")

    def test_should_raise_error_if_logged_in_employee_is_not_manager(self):
        non_manager = self.app_data.create_employee("employee1", "Employee", "User", "password1", "Normal")
        self.app_data.login(non_manager)
        with self.assertRaises(ValueError) as context:
            self.command.execute([])
        self.assertEqual(str(context.exception), "You are not manager,only Managers can view packages!")

    def test_should_return_no_unassigned_packages(self):
        result = self.command.execute([])
        self.assertEqual(result, "No unassigned packages")

    def test_should_return_unassigned_packages_list(self):
        locations_list = list(Locations.locations)
        if len(locations_list) < 2:
            start_loc = end_loc = locations_list[0]
        else:
            start_loc = locations_list[0]
            end_loc = locations_list[1]
        package = self.app_data.create_package("Test Customer", "0123456789", start_loc, end_loc, 5)
        
        result = self.command.execute([])
        expected_line = f"Package {package.id} is at Location: {package.start_loc}.\n"
        expected_result = "Unassigned packages:\n" + expected_line
        self.assertEqual(result, expected_result)
