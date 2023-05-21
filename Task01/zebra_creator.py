# Zebra emulation program
# Page zebracreator
# Stage 21 (Main task 1)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from zebra import Zebra

# объявляем класс
class ZebraCreator:
    @staticmethod
    def create(size=8):
        zebras = []
        num = 1

        for _ in range(size):
            # создаем экземпляр класса Zebra
            zebra = Zebra()
            zebra.name = "Zebra " + str(num)

            zebras.append(zebra)

            num += 1
        return zebras
