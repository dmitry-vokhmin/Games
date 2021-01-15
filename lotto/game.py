from basket import Basket
from userinterface import UserInterface
from user import User

class Game:
    __users = []

    def __init__(self):
        self.basket = Basket()

    def run_game(self):
        UserInterface.hello()
        players_amount = UserInterface.players_amount()
        self.create_user(players_amount)
        flag = False
        while not flag:
            try:
                basket_number = self.basket.get_number()
                UserInterface.basket(basket_number)
            except IndexError:
                UserInterface.gameover()
                break
            for user in self.__users:
                UserInterface.step(user)
                user.game_number(basket_number)
                UserInterface.user_cards(user.cards)
                UserInterface.win_card(user.end_numbers)
                flag = self.check_win()
        UserInterface.win()


    def create_user(self, players_amount):
        while players_amount:
            self.__users.append(User.create_user())
            players_amount -= 1

    def check_win(self):
        return UserInterface.check_win().lower() == "bingo"

a = Game()
a.run_game()