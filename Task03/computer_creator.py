# Computer emulation program
# Page class computercreator
# Stage 21 (Main task 3)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from random import choice, randint
from computer import Computer


class ComputerCreator:
    @staticmethod
    def create(size=15):
        computers = []
        BRAND = ("ASUS", "Lenovo", "Apple", "HP", "Samsung")

        MODEL_ASUS = ("Vivobook 16X", "ROG Strix G15", "TUF Gaming F15",
                      "VivoBook 14", "VivoBook Pro 15", "ROG Strix SCAR 16 2023")
        MODEL_LENOVO = ("Legion 5", "Legion 7", "IdeaPad Gaming 3",
                        "Legion 5 Pro", "Legion 7 Pro", "IdeaPad 3")
        MODEL_APPLE = ('Macbook Air 13" M1 2020', 'Macbook Air 13" M2 2022',
                       'Macbook Pro 14" M2 Pro 2023', 'Macbook Pro 14" M1 Max 2021',
                       'Macbook Pro 16" M1 Max 2021')
        MODEL_HP = ("HP Omen 17", "EliteBook 830 G9", "ZBook Fury 17 G8",
                    "255 G8", "250 G8")
        MODEL_SAMSUNG = ("Galaxy Book2 ", "Galaxy Book NP750",
                         "Galaxy Book Flex2 Alpha 13")

        MIN_PRICE = 390
        MAX_PRICE = 15987

        for _ in range(size):
            computer = Computer()
            computer.brand = choice(BRAND)

            if computer.brand == "ASUS":
                computer.model = choice(MODEL_ASUS)
            elif computer.brand == "Lenovo":
                computer.model = choice(MODEL_LENOVO)
            elif computer.brand == "Apple":
                computer.model = choice(MODEL_APPLE)
            elif computer.brand == "HP":
                computer.model = choice(MODEL_HP)
            elif computer.brand == "Samsung":
                computer.model = choice(MODEL_SAMSUNG)

            computer.price = randint(MIN_PRICE, MAX_PRICE)

            computers.append(computer)

        return computers
