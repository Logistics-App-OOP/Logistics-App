<<<<<<< HEAD
from core.application_data import ApplicationData
class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

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
=======
# from commands.login_command import LoginCommand
# from commands.logout_command import LogoutCommand
# from commands.register_employee_command import RegisterEmployeeCommand
# from commands.create_package import CreatePackage
# from commands.create_route import CreateRoute

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, cmd_name):
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
        
        raise ValueError('Invalid command name')
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
