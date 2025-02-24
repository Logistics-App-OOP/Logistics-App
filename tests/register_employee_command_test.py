import unittest
from commands.register_employee_command import RegisterEmployeeCommand
from core.application_data import Application_data

class RegisterEmployeeCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.app_data.login(self.app_data.employees[0])
        self.command = RegisterEmployeeCommand(self.app_data)

    def test_should_raise_error_if_not_logged_in(self):
        self.app_data.logout()
        with self.assertRaises(ValueError) as context:
            self.command.execute(['newuser', 'New', 'User', 'newpassword', 'Employee'])
        self.assertEqual(str(context.exception), 'You are not logged in! Please login first!')

    def test_should_raise_error_if_invalid_param_count_less(self):
        with self.assertRaises(ValueError) as context:
            self.command.execute(['newuser', 'New', 'User', 'newpassword'])
        self.assertEqual(
            str(context.exception),
            'Invalid number of arguments. Expected at least 5; received: 4.'
        )

    def test_should_raise_error_if_invalid_param_count_more(self):
        with self.assertRaises(ValueError) as context:
            self.command.execute(['newuser', 'New', 'User', 'newpassword', 'Employee', 'extra'])
        self.assertEqual(
            str(context.exception),
            "Invalid input!Expected: username,first name, last name, password, role."
        )
