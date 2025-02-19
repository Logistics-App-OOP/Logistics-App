import unittest

from models.employee import Employee

VALID_USERNAME = 'LYUBO123'
VALID_FIRST_NAME = 'Lyubo'
VALID_LAST_NAME = 'Parvanov'
VALID_PASSWORD = 'PASS12345'
VALID_ROLE = 'Normal'
class TestEmployee(unittest.TestCase):

    def test_employee_initialization(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        self.assertEqual(employee.username, VALID_USERNAME)
        self.assertEqual(employee.firstname, VALID_FIRST_NAME)
        self.assertEqual(employee.lastname, VALID_LAST_NAME)
        self.assertEqual(employee.password, VALID_PASSWORD)
        self.assertEqual(employee.role, VALID_ROLE)

    def test_username_setter_valid(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        employee.username = VALID_USERNAME
        self.assertEqual(employee.username, VALID_USERNAME)

    def test_username_setter_invalid_length(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.username = "l"  # too short
        with self.assertRaises(ValueError):
            employee.username = "l" * 21  # too long

    def test_username_setter_invalid_symbols(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.username = "LYU|BO"  # invalid symbol

    def test_password_valid(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        employee.password = VALID_PASSWORD
        self.assertEqual(employee.password, VALID_PASSWORD)

    def test_password_invalid_length(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.password = "1234"  # too short
        with self.assertRaises(ValueError):
            employee.password = "a" * 31  # too long

    def test_password_invalid_symbols(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.password = "password@123"  # invalid symbol

    def test_firstname_valid(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        employee.firstname = VALID_FIRST_NAME
        self.assertEqual(employee.firstname, VALID_FIRST_NAME)

    def test_firstname_invalid_length(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.firstname = "L"  # too short
        with self.assertRaises(ValueError):
            employee.firstname = "P" * 21  # too long

    def test_lastname_valid(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        employee.lastname = VALID_LAST_NAME
        self.assertEqual(employee.lastname, VALID_LAST_NAME)

    def test_lastname_invalid_length(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        with self.assertRaises(ValueError):
            employee.lastname = "S"  # too short
        with self.assertRaises(ValueError):
            employee.lastname = "a" * 21  # too long

    def test_is_manager(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        self.assertFalse(employee.is_manager())

        manager = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, 'Manager')
        self.assertTrue(manager.is_manager())

    def test_str_method(self):
        employee = Employee(VALID_USERNAME, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_PASSWORD, VALID_ROLE)
        self.assertEqual(str(employee), f"Username: {VALID_USERNAME}, Full Name: {VALID_FIRST_NAME} {VALID_LAST_NAME}"
                                        f", Role: {VALID_ROLE}")