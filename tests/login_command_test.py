import unittest
from commands.login_command import LoginCommand
from core.application_data import Application_data

class LoginCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.command = LoginCommand(self.app_data)
        self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")

    def test_should_login_successfully(self):
        result = self.command.execute(["Uasim1702", "123456789"])
        self.assertEqual(result, "Employee Uasim1702 successfully logged in!")
        self.assertEqual(self.app_data.logged_in_employee.username, "Uasim1702")

    def test_should_raise_error_if_no_username_or_password_provided(self):
        with self.assertRaises(ValueError):
            self.command.execute([])

        with self.assertRaises(ValueError):
            self.command.execute(["Uasim1702"])

        with self.assertRaises(ValueError):
            self.command.execute(["Uasim1702", "123456789", "extra_param"])

    def test_should_raise_error_if_wrong_password(self):
        with self.assertRaises(ValueError):
            self.command.execute(["Uasim1702", "wrongpassword"])

    def test_should_raise_error_if_user_not_found(self):
        with self.assertRaises(ValueError):
            self.command.execute(["UnknownUser", "123456789"])

    def test_should_raise_error_if_user_already_logged_in(self):
        self.command.execute(["Uasim1702", "123456789"])
        with self.assertRaises(ValueError):
            self.command.execute(["Uasim1702", "123456789"])
            