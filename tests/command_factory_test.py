import unittest
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_employee_command import RegisterEmployeeCommand
from commands.create_package_command import CreatePackage
from commands.create_route_command import CreateRouteCommand
from commands.find_routes_command import FindRoutes
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.assign_package_to_route_comand import AssignPackageToRoute
from commands.view_packages_command import ViewPackages
from commands.view_routes_command import ViewRoutes
from commands.view_trucks_command import ViewTrucks
from commands.find_package_command import FindPackage
from  core.command_factory import CommandFactory
from core.application_data import Application_data

class TestCommandFactory(unittest.TestCase):
    
    def setUp(self):
        self.app_data = Application_data()
        self.factory = CommandFactory(self.app_data)
    
    def test_create_login_command(self):
        command = self.factory.create('login')
        self.assertIsInstance(command, LoginCommand)
    
    def test_create_logout_command(self):
        command = self.factory.create('logout')
        self.assertIsInstance(command, LogoutCommand)
    
    def test_create_register_employee_command(self):
        command = self.factory.create('registeremployee')
        self.assertIsInstance(command, RegisterEmployeeCommand)
    
    def test_create_create_package_command(self):
        command = self.factory.create('createpackage')
        self.assertIsInstance(command, CreatePackage)
    
    def test_create_create_route_command(self):
        command = self.factory.create('createroute')
        self.assertIsInstance(command, CreateRouteCommand)
    
    def test_create_find_routes_command(self):
        command = self.factory.create('findroutes')
        self.assertIsInstance(command, FindRoutes)
    
    def test_create_assign_truck_to_route_command(self):
        command = self.factory.create('assigntrucktoroute')
        self.assertIsInstance(command, AssignTruckToRoute)
    
    def test_create_assign_package_to_route_command(self):
        command = self.factory.create('assignpackagetoroute')
        self.assertIsInstance(command, AssignPackageToRoute)
    
    def test_create_view_packages_command(self):
        command = self.factory.create('viewpackages')
        self.assertIsInstance(command, ViewPackages)
    
    def test_create_view_routes_command(self):
        command = self.factory.create('viewroutes')
        self.assertIsInstance(command, ViewRoutes)
    
    def test_create_view_trucks_command(self):
        command = self.factory.create('viewtrucks')
        self.assertIsInstance(command, ViewTrucks)
    
    def test_create_find_package_command(self):
        command = self.factory.create('findpackage')
        self.assertIsInstance(command, FindPackage)
    
    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            self.factory.create('invalidcommand')
