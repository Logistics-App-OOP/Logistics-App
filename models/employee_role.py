class EmployeeRole:
    NORMAL = 'Normal'
    MANAGER = 'Manager'

<<<<<<< HEAD
    def from_string(value) -> str:
        if value not in [EmployeeRole.NORMAL, EmployeeRole.MANAGER]:
            raise ValueError(
                f'The role you entered {value} is not supported.')
=======
    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.NORMAL, cls.MANAGER]:
            raise ValueError(
                f'None of the possible Employee Roles values matches the value {value}.')
>>>>>>> b395aa0 (Updated main based on Emil's branch)

        return value