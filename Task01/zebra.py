# Zebra emulation program
# Page zebra
# Stage 21 (Main task 1)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

# объявляем класс
class Zebra:
    def __init__(self, name='Zebra', stripe=True):
        self.__name = name
        self.__stripe = stripe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # задаем условия
        if isinstance(name, str):
            self.__name = name

    @property
    def stripe(self):
        # задаем условия
        if self.__stripe:
            self.__stripe = False
            return False
        else:
            self.__stripe = True
            return True

    def __str__(self):
        return f"{self.name} - " \
            + ("white line" if self.stripe else "black line")
