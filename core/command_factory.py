
class CommandFactory:
    def __init__(self, data):
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
