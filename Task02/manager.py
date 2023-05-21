# Human emulation program
# Page manager
# Stage 21 (Main task 2)
# Subject theme: Python Object-Oriented Programming. Encapsulation
# Version: 1.0
# Autor: Ilja
# Date: 10.05.2023

from human import Human


class Manager:
    @staticmethod
    def count_adult(humans):
        if isinstance(humans, (list, tuple)):
            count = 0

            for human in humans:
                if isinstance(human, Human) and human.age >= 18:
                    count += 1
            return count

    @staticmethod
    def count_underage(humans):
        if isinstance(humans, (list, tuple)):
            total = len(humans)
            total -= Manager.count_adult(humans)

            return total

    @staticmethod
    def count_alive(humans):
        if isinstance(humans, (list, tuple)):
            count = 0

            for human in humans:
                if isinstance(human, Human) and human.is_alive == "Yes":
                    count += 1
            return count

    @staticmethod
    def count_dead(humans):
        if isinstance(humans, (list, tuple)):
            total = len(humans)
            total -= Manager.count_alive(humans)

            return total
