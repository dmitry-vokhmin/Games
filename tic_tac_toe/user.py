from user_interface import UserInterface

class User:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def user_step(self, board):
        while True:
            coords = UserInterface.step(self)
            if not board[coords[0]][coords[1]]:
                break
            print("Ячейка занята, повторите ввод")
        return coords

    @classmethod
    def create_user(cls, symbol):
        name = input(f"Введите свое имя с символом {symbol}\n")
        UserInterface.hello_user(name, symbol)
        return cls(name.title(), symbol)


