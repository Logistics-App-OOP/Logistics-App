from models.employee_role import EmployeeRole

class Employee:
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

<<<<<<< HEAD
=======
    NOT_SUPERVISOR_ERROR = "Only supervisors are granted access."
    NOT_MANAGER_ERROR = "Only managers are granted access."


>>>>>>> b395aa0 (Updated main based on Emil's branch)
    def __init__(self, username, firstname, lastname, password, role):
        self.username = username
        self.password = password
        self.lastname = lastname
        self.firstname = firstname
<<<<<<< HEAD
        self._role = EmployeeRole.from_string(role)
        
    @property
    def role(self):
        return self._role
=======
        self.role = role
>>>>>>> b395aa0 (Updated main based on Emil's branch)
    
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
    
    @property
    def is_manager(self):
        if self.role == EmployeeRole.MANAGER:
            return True
        return False
    
    def __str__(self):
        return f'Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.role}'