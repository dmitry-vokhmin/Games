from userinterface import UserInterface
from card import CardGenerate

class User:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.end_numbers = []

    def game_number(self, number):
        for itm in self.cards:
            if number in itm:
                self.end_numbers.append(number)
                UserInterface.end_number(number)

    @classmethod
    def create_user(cls):
        name = UserInterface.create_user()
        cards = CardGenerate().get_card(UserInterface.cards_amount())
        UserInterface.user_cards(cards)
        return cls(name.title(), cards)