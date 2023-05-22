# Zebra emulation program
# Page main
# Stage 21 (Main task 1)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from zebra import Zebra
from zebra_creator import ZebraCreator


# задание функции и ее параметров
def main():
    # инициализация переменной и её значений
    z1 = Zebra()
    # вывод результатов
    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print(z1)
    print()
    # запрос списка
    ls = ZebraCreator.create()
    # задаем условие
    for zebra in ls:
        # вывод результатов
        print(zebra)
    print()
    # задаем условие
    for zebra in ls:
        # вывод результатов
        print(zebra)
    print()
    # задаем условие
    for zebra in ls:
        # вывод результатов
        print(zebra)
        print(zebra)


if __name__ == '__main__':
    main()


# задание функции и условий теста
def test():
    result = "\nZebra - black line - " + str(Zebra() == {"Zebra - black line"})
    result += "\nZebra - white line - " + str(Zebra() == {"Zebra - white line"})
    result += "\nZebra - black line - " + str(Zebra() == "Zebra - black line")
    result += "\nZebra - white line - " + str(Zebra() == "Zebra - white line")
    result += "\nZebra - black line - " + str(Zebra() == "Zebra - black line")
    result += "\nZebra - white line - " + str(Zebra() == "Zebra - white line")
    # вывод результата
    print(result)


if __name__ == "__main__":
    test()

