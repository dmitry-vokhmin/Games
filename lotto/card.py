import random

class CardGenerate:
    def __init__(self):
        self.__cards = set()

    def get_card(self, card_amount):
        return self.__create_card(card_amount)

    def __create_card(self, card_amount):
        result = []
        while len(result) != card_amount:
            card = Card()
            if card not in self.__cards:
                self.__cards.add(card)
                result.append(card)
        return result


class Card:
    def __init__(self):
        self.numbers = self.__random_generate()


    def __random_generate(self):
        card = set()
        while len(card) != 15:
            card.add(random.randint(1, 100))
        return tuple(card)

    def __hash__(self):
        return hash(self.numbers)

    def __iter__(self):
        return self.numbers.__iter__()

    def __getitem__(self, item):
        return self.numbers[item]

    def __str__(self):
        result = ""
        for itm in self:
            result += str(itm) + ","
        return result