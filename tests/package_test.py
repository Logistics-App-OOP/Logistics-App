import unittest
from models.package import Package
from models.locations import Locations

VALID_CUSTOMER_NAME = "Uasim"
VALID_PHONE = "0404040404"
VALID_START_LOC = "Sydney"
VALID_END_LOC = "Melbourne"
VALID_WEIGHT = 45

class Package_should(unittest.TestCase):

    def setUp(self):
        Locations.locations = ["Sydney", "Melbourne", "Brisbane", "Adelaide", "Perth"]

    def test_should_assignValuesProperly(self):
        package = Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_START_LOC, VALID_END_LOC, VALID_WEIGHT)
        self.assertEqual(package.customer_name, VALID_CUSTOMER_NAME)
        self.assertEqual(package.customer_phone, VALID_PHONE)
        self.assertEqual(package.start_loc, VALID_START_LOC)
        self.assertEqual(package.end_loc, VALID_END_LOC)
        self.assertEqual(package.weight, VALID_WEIGHT)
        self.assertEqual(package.status, "Created")

    def test_init_should_RaiseError_WithInvalidStartLocation(self):
        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, VALID_PHONE, "InvalidCity", VALID_END_LOC, VALID_WEIGHT)

    def test_init_should_RaiseError_WithInvalidEndLocation(self):
        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_START_LOC, "UnknownCity", VALID_WEIGHT)

    def test_init_should_RaiseError_WithInvalidPhoneNumber(self):
        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, "04040abcde", VALID_START_LOC, VALID_END_LOC, VALID_WEIGHT)

    def test_init_should_RaiseError_WithInvalidPhoneLength(self):
        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, "04040404", VALID_START_LOC, VALID_END_LOC, VALID_WEIGHT)

        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, "040404040404", VALID_START_LOC, VALID_END_LOC, VALID_WEIGHT)

    def test_init_should_RaiseError_WithInvalidWeight(self):
        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_START_LOC, VALID_END_LOC, -10)

        with self.assertRaises(ValueError):
            Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_START_LOC, VALID_END_LOC, 0)

    def test_should_checkUpdateStatusWorksProperly(self):
        package = Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_START_LOC, VALID_END_LOC, VALID_WEIGHT)
        self.assertEqual(package.status, "Created")
        package.update_status()
        self.assertEqual(package.status, "In Transit")