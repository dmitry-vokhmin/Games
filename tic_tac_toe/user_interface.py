class UserInterface:
    @staticmethod
    def hello():
        print("Добро пожаловать в игру крестики нолики\n")

    @staticmethod
    def game_mod():
        while True:
            try:
                game_mod = int(input("Выберите режим игры\n"
                                     "Введите 1 для игры с компьютером или 2 для игры с игроком\n"))
            except ValueError:
                print("Введенно не число, повторите ввод\n")
                continue
            if game_mod == 1 or game_mod == 2:
                return game_mod
            print("Вы ввели не правильную цифру\n")

    @staticmethod
    def create_user_name(symbol):
        name = input(f"Введите свое имя с символом {symbol}\n")
        return name

    @staticmethod
    def hello_user(name, symbol):
        print(f"Игрок с именем: {name} и символом: {symbol} создан\n")

    @staticmethod
    def create_bot(name, symbol):
        print(f"Компьютер с именем: {name} и символом: {symbol} создан\n")

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
    def step_bot(coords):
        print(f"Компьютер сходил на клетку {coords[0] + 1}, {coords[1] + 1}")

    @staticmethod
    def win_game(user):
        print(f"{user.name} выйграл")

    @staticmethod
    def standoff():
        print("Ничья - победителя нет")
