import unittest
from datetime import datetime

from core.application_data import Application_data

class Application_data_should(unittest.TestCase):
    
    def setUp(self):
        self.app_data = Application_data()
    
    def test_should_CreateEmployeeProperly(self):
        employee = self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
        self.assertEqual(employee.username, "Uasim1702")
        self.assertEqual(employee.firstname, "Uasim")
        self.assertEqual(employee.lastname, "Halak")
        self.assertEqual(employee.role, "Manager")
        self.assertIn(employee, self.app_data.employees)
    
    def test_should_raise_error_IfDuplicatedEmployee(self):
        self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
        with self.assertRaises(ValueError):
            self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
             
             
    def test_should_CreatePackageProperly(self):
        package = self.app_data.create_package("Uasim", "0876417576", "Sydney", "Melbourne", 50)
        self.assertEqual(package.customer_name, "Uasim")
        self.assertEqual(package.customer_phone, "0876417576")
        self.assertEqual(package.start_loc, "Sydney")
        self.assertEqual(package.end_loc, "Melbourne")
        self.assertEqual(package.weight, 50)
        self.assertIn(package, self.app_data.packages)
        
        
    def test_should_FindPackageById(self):
        package = self.app_data.create_package("Uasim", "0876417576", "Melbourne", "Brisbane", 30)
        found_package = self.app_data.find_package_by_id(package.id)
        self.assertEqual(found_package, package)

    def test_find_package_returns_error_IfPackageDoesNot_exist(self):
        with self.assertRaises(ValueError):
            self.app_data.find_package_by_id(500)
            
    def test_should_createRouteProperly(self):
        departure_time = datetime(2025, 2, 10, 14, 30)
        route = self.app_data.create_route(departure_time, "Sydney", "Melbourne", "Adelaide")
        self.assertEqual(route.departure_time, departure_time)
        self.assertEqual(route.locations, ["Sydney", "Melbourne", "Adelaide"])
        self.assertIn(route, self.app_data.routes)

    def test_should_findRouteById(self):
        departure_time = datetime(2025, 2, 11, 10, 0)
        route = self.app_data.create_route(departure_time, "Brisbane", "Darwin")
        found_route = self.app_data.find_route_by_id(route.id)
        self.assertEqual(found_route, route)

    def test_should_raise_error_ifFindRouteDoesNotExist(self):
        with self.assertRaises(ValueError):
            self.app_data.find_route_by_id(500)

    def test_should_createEmployeeProperly(self):
        employee = self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Normal")
        self.assertEqual(employee.username, "Uasim1702")
        self.assertEqual(employee.firstname, "Uasim")
        self.assertEqual(employee.lastname, "Halak")
        self.assertEqual(employee.password, "123456789")
        self.assertEqual(employee.role, "Normal")

    def test_should_loginAndLogoutProperly(self):
        employee = self.app_data.create_employee("Uasim1702", "Uasim", "Halak", "123456789", "Manager")
        self.app_data.login(employee)
        self.assertEqual(self.app_data.logged_in_employee, employee)
        self.app_data.logout()
        self.assertFalse(self.app_data.has_logged_in_employee)

    def test_should_checkTruckAvailabilityAndRange(self):
        truck = self.app_data.check_truck_has_enough_range_and_is_available(5000)
        self.assertTrue(truck.available)
        self.assertTrue(truck.max_range >= 5000)
        truck.assign_to_route("1")
        self.assertFalse(truck.available)

    def test_should_raise_error_IfTruckRangeNotSuitable(self):
        with self.assertRaises(ValueError):
            self.app_data.check_truck_has_enough_range_and_is_available(20000)