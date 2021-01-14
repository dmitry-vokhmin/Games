class Board:
    def __init__(self):
        self.__board = [[0, 0, 0] for _ in range(3)]

    def set_step(self, user_step, user):
        self.__board[user_step[0]][user_step[1]] = user

    def __iter__(self):
        return self.__board.__iter__()

    def __getitem__(self, item):
        return self.__board[item]

    def __len__(self):
        return len(self.__board)

    def __str__(self):
        result = "# 1 2 3\n"
        line = 1
        for itm in self:
            result += f"{line} " + " ".join(map(lambda x: str(x) if not x else x.symbol, itm)) + "\n"
            line += 1
        return result
