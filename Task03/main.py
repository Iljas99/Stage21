# Computer emulation program
# Page main
# Stage 21 (Main task 3)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from computer_creator import ComputerCreator
from manager import Manager


def main():
    ls = ComputerCreator.create()
    for computer in ls:
        print(computer)

    total_cost = Manager.count_total_cost(ls)

    max_price = Manager.max_price(ls)

    min_price = Manager.min_price(ls)
    print(f"Total cost: {total_cost}$"
          f"\nMaximum cost: {max_price}$"
          f"\nMinimum cost: {min_price}$")


if __name__ == '__main__':
    main()
