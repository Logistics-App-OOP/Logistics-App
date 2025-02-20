import unittest
from commands.logout_command import LogoutCommand
from core.application_data import Application_data
from models.employee import Employee

class LogoutCommand_should(unittest.TestCase):

    def setUp(self):
        self.app_data = Application_data()
        self.command = LogoutCommand(self.app_data)
        self.employee = self.app_data.create_employee("Uasim17022", "Uasim", "Halak", "123456789", "Manager")

    def test_should_logout_successfully(self):
        self.app_data.login(self.employee)
        result = self.command.execute([])
        self.assertEqual(result, "You logged out!")
        self.assertFalse(self.app_data.has_logged_in_employee)

    def test_should_raise_error_if_not_logged_in(self):
        with self.assertRaises(ValueError):
            self.command.execute([])

    def test_should_raise_error_if_extra_input_given(self):
        self.app_data.login(self.employee)
        with self.assertRaises(ValueError):
            self.command.execute(["extra_param"])
