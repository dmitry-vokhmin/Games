class UserInterface:
    @staticmethod
    def hello():
        print("Добро пожаловать в игру лато\n")

    @staticmethod
    def players_amount():
        while True:
            try:
                players_amount = int(input("Введите количество игроков от 1 до 5, например: 2\n"))
            except ValueError:
                print("Введено не число, повторите ввод\n")
                continue
            if 1 <= players_amount <= 5:
                return players_amount
            else:
                print("Число должно быть от 1 до 5, повторите ввод\n")
                continue


    @staticmethod
    def create_user():
        name = input("Введите свое имя\n")
        return name

    @staticmethod
    def cards_amount():
        while True:
            try:
                cards_amount = int(input("Сколько карточек вы хотите взять от 1 до 5, например: 2\n"))
            except ValueError:
                print("Введено не число, повторите ввод\n")
                continue
            if 1 <= cards_amount <= 5:
                return cards_amount
            else:
                print("Число должно быть от 1 до 5, повторите ввод\n")
                continue

    @staticmethod
    def user_cards(cards):
        for itm in cards:
            print(f"Ваш набор карточек: {itm}\n")

    @staticmethod
    def step(user):
        print(f"Сейчас ходит игрок: {user.name}\n")

    @staticmethod
    def win_card(card):
        print(f"Числа которые вы зачеркнули: {card}\n")

    @staticmethod
    def basket(number):
        print(f"Выпало число: {number}\n")

    @staticmethod
    def end_number(number):
        print(f"У вас есть это число: {number}\n")

    @staticmethod
    def check_win():
        bingo = input("Если вы собрали все числа с хотя бы одной карточки напишите 'bingo', если нет то нажмите enter\n")
        return bingo

    @staticmethod
    def win():
        print("Вы выйграли, поздравляю!!!")

    @staticmethod
    def gameover():
        print("Игра  закончилась")