class EmployeeRole:
    NORMAL = 'Normal'
    MANAGER = 'Manager'

    def from_string(value) -> str:
        if value not in [EmployeeRole.NORMAL, EmployeeRole.MANAGER]:
            raise ValueError(
                f'The role you entered {value} is not supported.')

        return value
