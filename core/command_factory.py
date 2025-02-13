
import cmd
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_employee_command import RegisterEmployeeCommand
from commands.create_package_command import CreatePackage
from commands.create_route_command import CreateRouteCommand
from commands.find_routes_command import FindRoutes

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
        
        raise ValueError('Invalid command name')
