class EmployeeRole:
    NORMAL = 'Normal'
    MANAGER = 'Manager'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.NORMAL, cls.MANAGER]:
            raise ValueError(
                f'None of the possible Employee Roles values matches the value {value}.')

        return value