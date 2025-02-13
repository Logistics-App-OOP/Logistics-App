from commands.base_command import BaseCommand

class ViewPackageInfo(BaseCommand):

    def execute(self, params):
        super().execute(params)
        return self._app_data.view_package_info()
    
    def _requires_login(self) -> bool:
        return True
    
    def _expected_params_count(self) -> int:
        return 0
    
    def _requires_supervisor(self) -> bool:
        return True
    
    def _requires_manager(self) -> bool:
        return False