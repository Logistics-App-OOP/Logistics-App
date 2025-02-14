<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4c07a03 (Created CreateRoute)
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_employee_command import RegisterEmployeeCommand
from commands.create_package_command import CreatePackage
from commands.create_route_command import CreateRouteCommand
<<<<<<< HEAD
from commands.find_routes_command import FindRoutes
from commands.assign_truck_to_route import AssignTruckToRoute
from commands.assign_package_to_route_comand import AssignPackageToRoute
from commands.view_packages_command import ViewPackages
from commands.view_routes_command import ViewRoutes
from commands.view_trucks_command import ViewTrucks
from commands.find_package_command import FindPackage
=======
# from commands.login_command import LoginCommand
# from commands.logout_command import LogoutCommand
# from commands.register_employee_command import RegisterEmployeeCommand
# from commands.create_package import CreatePackage
# from commands.create_route import CreateRoute
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
>>>>>>> 4c07a03 (Created CreateRoute)
=======
>>>>>>> 272ca14 (uasim's branch)

=======
=======
>>>>>>> e6a5d05 (Created truck editted app_data, route,package)
=======
>>>>>>> 4b32701 (Created CreateRoute)
from core.application_data import ApplicationData
>>>>>>> e431c9e (update branch)
class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

<<<<<<< HEAD
    def create(self, cmd_name):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4c07a03 (Created CreateRoute)
        if cmd_name.lower() == 'login':
            return LoginCommand(self._app_data)
        if cmd_name.lower() == 'logout':
            return LogoutCommand(self._app_data)
        if cmd_name.lower() == 'registeremployee':
            return RegisterEmployeeCommand(self._app_data)
        if cmd_name.lower() == 'createpackage':
            return CreatePackage(self._app_data)
        if cmd_name.lower() == 'createroute':
            return CreateRouteCommand(self._app_data)
<<<<<<< HEAD
        if cmd_name.lower() == 'findroutes':
            return FindRoutes(self._app_data)
        if cmd_name.lower() == 'assigntrucktoroute':
            return AssignTruckToRoute(self._app_data)
        if cmd_name.lower() == 'assignpackagetoroute':
            return AssignPackageToRoute(self._app_data)
        if cmd_name.lower() == 'viewpackages':
            return ViewPackages(self._app_data)
        if cmd_name.lower() == 'viewroutes':
            return ViewRoutes(self._app_data)
        if cmd_name.lower() == 'viewtrucks':
            return ViewTrucks(self._app_data)
        if cmd_name.lower() == 'findpackage':
            return FindPackage(self._app_data)
        raise ValueError('Invalid command name')
=======
        # if cmd_name.upper() == 'LOGIN':
        #     return LoginCommand(self._app_data)
        # if cmd_name.upper() == 'LOGOUT':
        #     return LogoutCommand(self._app_data)
        # if cmd_name.upper() == 'REGISTEREMPLOYEE':
        #     return RegisterEmployeeCommand(self._app_data)
        # if cmd_name.upper() == 'CREATEPACKAGE':
        #     return CreatePackage(self._app_data)
        # if cmd_name.upper() == 'CREATEROUTE':
        #     return CreateRoute(self._app_data)
=======
>>>>>>> 4c07a03 (Created CreateRoute)
        
        raise ValueError('Invalid command name')
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
=======
    # def create(self, cmd_name):
    #     if cmd_name.upper() == 'LOGIN':
    #         return LoginCommand(self._app_data)
    #     if cmd_name.upper() == 'LOGOUT':
    #         return LogoutCommand(self._app_data)
    #     if cmd_name.upper() == 'SHOWUSERS':
    #         return ShowUsersCommand(self._app_data)
    #     if cmd_name.upper() == 'ADDCOMMENT':
    #         return AddCommentCommand(self._app_data)
    #     if cmd_name.upper() == 'ADDVEHICLE':
    #         return AddVehicleCommand(self._app_data)
    #     if cmd_name.upper() == 'REGISTERUSER':
    #         return RegisterUserCommand(self._app_data)
    #     if cmd_name.upper() == 'SHOWVEHICLES':
    #         return ShowVehiclesCommand(self._app_data)
    #     if cmd_name.upper() == 'REMOVECOMMENT':
    #         return RemoveCommentCommand(self._app_data)
    #     if cmd_name.upper() == 'REMOVEVEHICLE':
    #         return RemoveVehicleCommand(self._app_data)

        raise ValueError('Invalid command name')
<<<<<<< HEAD
>>>>>>> 272ca14 (uasim's branch)
=======
=======
# from commands.login_command import LoginCommand
# from commands.logout_command import LogoutCommand
# from commands.register_employee_command import RegisterEmployeeCommand
# from commands.create_package import CreatePackage
# from commands.create_route import CreateRoute
=======
=======

>>>>>>> 5657f45 (Rebased from main)
=======
import cmd
>>>>>>> 9b3c1fa (created find routes and create routes)
=======
>>>>>>> 3588a2d (Created assigntrucktoroute added all files needed for the project added some commands in appdata and fixed output if invalid city is entered.)
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

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, cmd_name):
        if cmd_name.lower() == 'login':
            return LoginCommand(self._app_data)
        if cmd_name.lower() == 'logout':
            return LogoutCommand(self._app_data)
        if cmd_name.lower() == 'registeremployee':
            return RegisterEmployeeCommand(self._app_data)
        if cmd_name.lower() == 'createpackage':
            return CreatePackage(self._app_data)
        if cmd_name.lower() == 'createroute':
            return CreateRouteCommand(self._app_data)
        if cmd_name.lower() == 'findroutes':
            return FindRoutes(self._app_data)
        if cmd_name.lower() == 'assigntrucktoroute':
            return AssignTruckToRoute(self._app_data)
        if cmd_name.lower() == 'assignpackagetoroute':
            return AssignPackageToRoute(self._app_data)
        if cmd_name.lower() == 'viewpackages':
            return ViewPackages(self._app_data)
        if cmd_name.lower() == 'viewroutes':
            return ViewRoutes(self._app_data)
        if cmd_name.lower() == 'viewtrucks':
            return ViewTrucks(self._app_data)
        if cmd_name.lower() == 'findpackage':
            return FindPackage(self._app_data)
        raise ValueError('Invalid command name')
<<<<<<< HEAD
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
>>>>>>> e6a5d05 (Created truck editted app_data, route,package)
=======
>>>>>>> 5657f45 (Rebased from main)
