# Computer emulation program
# Page manager
# Stage 21 (Main task 3)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from computer import Computer


class Manager:
    @staticmethod
    def count_total_cost(computers):
        if isinstance(computers, (list, tuple)):
            total_cost = 0
            for computer in computers:
                if isinstance(computer, Computer):
                    total_cost += computer.price

            return total_cost

    @staticmethod
    def max_price(computers):
        if isinstance(computers, (list, tuple)):
            max_price = computers[0].price
            for computer in computers:
                if isinstance(computer, Computer) and max_price < computer.price:
                    max_price = computer.price

            return max_price

    @staticmethod
    def min_price(computers):
        if isinstance(computers, (list, tuple)):
            min_price = Manager.max_price(computers)
            for computer in computers:
                if isinstance(computer, Computer) and min_price > computer.price:
                    min_price = computer.price

            return min_price
