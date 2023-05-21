# Human emulation program
# Page humancreator
# Stage 21 (Main task 2)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from random import choice, randint
from human import Human
from string import ascii_uppercase


class HumanCreator:
    @staticmethod
    def create(size=10):
        humans = []
        NAMES = ("Alex", "Peter", "Garry", "Alice", "Vladimir",
                 "Olga", "Anna", "Kate", "Victor", "Max")

        MAX_AGE = 120
        MIN_AGE = 1

        for _ in range(size):
            human = Human()
            human.name = choice(NAMES)
            human.name += " " + choice(ascii_uppercase) + "."

            human.age = randint(MIN_AGE, MAX_AGE)

            human.is_alive = choice((True, False))

            humans.append(human)
        return humans
