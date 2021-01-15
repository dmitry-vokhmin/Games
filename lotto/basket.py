import random

class Basket:
    def __init__(self):
        self.__basket = list(range(1, 100))

    def get_number(self):
        random.shuffle(self.__basket)
        return self.__basket.pop()

    def __str__(self):
        return str(self.get_number())