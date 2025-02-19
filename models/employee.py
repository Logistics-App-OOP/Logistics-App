from models.employee_role import EmployeeRole

class Employee:
    """
    Represents an Employee with a username, first name, last name, password, role.
    """
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    def __init__(self, username, firstname, lastname, password, role):
        """
        Initializes an instance of the Class Employee.

        Args:
        username (str)
        firstname(str)
        lastname(str)
        password(str)
        role(str): only needs to be specified if Manager, otherwise defaults to Normal.

        Raises:
        ValueError: if invalid username.
        ValueError: if invalid firstname.
        ValueError: if invalid lastname.
        ValueError: if invalid password.
        ValueError: if invalid role.
        """
        self.username = username
        self.password = password
        self.lastname = lastname
        self.firstname = firstname
        self._role = EmployeeRole.from_string(role)
        
    @property
    def role(self):
        return self._role
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if len(value) < Employee.USERNAME_LEN_MIN or len(value) > Employee.USERNAME_LEN_MAX:
            raise ValueError(Employee.USERNAME_LEN_ERR)
        if not value.isalnum():
            raise ValueError(Employee.USERNAME_INVALID_SYMBOLS)
        self._username = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if len(value) < Employee.PASSWORD_LEN_MIN or len(value) > Employee.PASSWORD_LEN_MAX:
            raise ValueError(Employee.PASSWORD_LEN_ERR)
        if not value.isalnum():
            raise ValueError(Employee.PASSWORD_INVALID_SYMBOLS)
        self._password = value
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, value):
        if len(value) < Employee.FIRSTNAME_LEN_MIN or len(value) > Employee.FIRSTNAME_LEN_MAX:
            raise ValueError(Employee.FIRSTNAME_LEN_ERR)
        self._firstname = value
    
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value):
        if len(value) < Employee.LASTNAME_LEN_MIN or len(value) > Employee.LASTNAME_LEN_MAX:
            raise ValueError(Employee.LASTNAME_LEN_ERR)
        self._lastname = value
    
    def is_manager(self):
        """
        Checks employee role.

        Returns:
        True: if it's manager.
        False: if it's normal.
        """
        if self.role == EmployeeRole.MANAGER:
            return True
        return False
    
    def __str__(self):
        return f'Username: {self.username}, Full Name: {self.firstname} {self.lastname}, Role: {self.role}'
