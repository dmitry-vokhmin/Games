from user_interface import UserInterface

class User:
    def __init__(self, name, symbol, is_bot=False):
        self.name = name
        self.symbol = symbol
        self.is_bot = is_bot

    def user_step(self, board):
        if self.is_bot:
            coords = self.bot_step(board)
            UserInterface.step_bot(coords)
        else:
            while True:
                coords = UserInterface.step(self)
                if not board[coords[0]][coords[1]]:
                    break
                print("Ячейка занята, повторите ввод")
        return coords

    def bot_step(self, board):
        diagonal = [board[idx][idx] for idx in range(0, 3)]
        if self.is_diagonal_bot(diagonal) or self.is_diagonal_user(diagonal):
            coords = diagonal.index(0), diagonal.index(0)
            return coords
        diagonal = [board[line_idx][idx]for line_idx, idx in zip(range(0, 3), range(2, -1, -1))]
        if self.is_diagonal_bot(diagonal) or self.is_diagonal_user(diagonal):
            coords = diagonal.index(0), abs(diagonal.index(0) - 2)
            return coords
        return self.check_step_ver_and_hor(board)

    @staticmethod
    def check_step_ver_and_hor(board, symbol1="o", symbol2=0):
        while True:
            line = 0
            for elem in zip(board, zip(*board)):
                for itm in elem:
                    if itm.count(symbol1) == len(itm) - 1 and itm.count(symbol2):
                        coords = (line, itm.index(0)) if itm is elem[0] else (itm.index(0), line)
                        return coords
                line += 1
            if symbol1 == "o":
                symbol1 = "x"
            elif symbol1 == "x":
                symbol1 = 0
                symbol2 = "o"
            else:
                return (1, 1) if board[1][1] != "x" else (0, 0)

    @staticmethod
    def is_diagonal_user(line):
        return line.count("x") == len(line) - 1 and not line.count("o")

    @staticmethod
    def is_diagonal_bot(line):
        return line.count("o") == len(line) - 1 and not line.count("x")

    @classmethod
    def create_user(cls, symbol):
        name = UserInterface.create_user_name(symbol)
        UserInterface.hello_user(name, symbol)
        return cls(name.title(), symbol)

    @classmethod
    def create_bot(cls, symbol):
        name = "Hitman"
        UserInterface.create_bot(name, symbol)
        return cls(name, symbol, is_bot=True)

