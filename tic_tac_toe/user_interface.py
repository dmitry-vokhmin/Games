class UserInterface:
    @staticmethod
    def hello():
        print("Добро пожаловать в игру крестики нолики\n")

    @staticmethod
    def hello_user(name, symbol):
        print(f"Игрок с именем: {name} и символом: {symbol} создан\n")

    @staticmethod
    def step(user):
        print(f"Сейчас ходит игрок: {user.name}, его символ: {user.symbol}")
        while True:
            coords = input("Введите координаты точки через пробел\n")
            try:
                coords = [int(itm) - 1 for itm in coords.split(" ") if itm.isdigit()]
            except ValueError:
                print("Что то введено не верно")
                continue
            if not coords:
                print("Не правильный ввод")
                continue
            return coords

    @staticmethod
    def board(board):
        result = "# 1 2 3\n"
        line = 1
        for itm in board:
            result += f"{line} " + " ".join(map(str, itm)) + "\n"
            line += 1
        print(result)

    @staticmethod
    def win_game(user):
        print(f"{user.name} выйграл")

    @staticmethod
    def standoff():
        print("Ничья - победителя нет")
