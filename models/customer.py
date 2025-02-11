
class Customer:

    def __init__(self, name, number):
        if len(name) < 2 or len(name) > 15:
            raise ValueError('Invalid name: Name must be at least 2 symbols long.')
        self._name = name
        if not len(number) == 10 and not number.isdigit():
            raise ValueError("Invalid number: Number must contains only digits.")
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number


