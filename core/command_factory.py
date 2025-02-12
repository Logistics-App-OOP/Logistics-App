from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.register_employee_command import RegisterEmployeeCommand
from commands.create_package import CreatePackage
from commands.create_route import CreateRoute

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, cmd_name):
        if cmd_name.upper() == 'LOGIN':
            return LoginCommand(self._app_data)
        if cmd_name.upper() == 'LOGOUT':
            return LogoutCommand(self._app_data)
        if cmd_name.upper() == 'REGISTEREMPLOYEE':
            return RegisterEmployeeCommand(self._app_data)
        if cmd_name.upper() == 'CREATEPACKAGE':
            return CreatePackage(self._app_data)
        if cmd_name.upper() == 'CREATEROUTE':
            return CreateRoute(self._app_data)
        
        raise ValueError('Invalid command name')
