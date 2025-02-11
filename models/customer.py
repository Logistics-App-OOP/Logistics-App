
class Customer:

    def __init__(self, first, surname, number):
        if len(first) < 3 or len(first) > 15:
            raise ValueError('Invalid name: name must be at least 3 symbols long.')
        self._first = first
        if len(surname) < 3 or len(surname) > 15:
            raise ValueError('Invalid surname: name must be at least 3 symbols long.')
        self._surname = surname
        if not number.isdigit():
            raise ValueError("Invalid number: Number must contains only digits.")
        self._number = number

    @property
    def first(self):
        return self._first.capitalize()

    @property
    def surname(self):
        return self._surname.capitalize()

    @property
    def number(self):
        return self._number

    def __str__(self):
        return (f"First name: {self._first}\n"
                f"Surname: {self._surname}\n"
                f"Contact number: {self._number}")