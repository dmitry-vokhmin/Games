class UserInterface:
    @staticmethod
    def hello():
        print("Добро пожаловать в игру крестики нолики")

    @staticmethod
    def step(user):
        print(f"Сейчас ходит игрок: {user.name}, его символ: {user.symbol}")
        while True:
            coords = input("Введите координаты точки через пробел\n")
            try:
                coords = [int(itm) for itm in coords.split(" ") if itm.isdigit()]
            except ValueError:
                print("Что то введено не верно")
                continue
            if not coords:
                print("Не правильный ввод")
                continue
            return coords

    @staticmethod
    def board(board):
        result = ""
        for itm in board:
            result += " ".join(map(str, itm)) + "\n"
        print(result)

    @staticmethod
    def win_game(user):
        print(f"{user.name} выйграл")

    @staticmethod
    def standoff():
        print("Ничья - победителя нет")
