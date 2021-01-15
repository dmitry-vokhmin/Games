from itertools import cycle
from user import User
from board import Board
from user_interface import UserInterface


class Game:
    __users = []

    def __init__(self):
        self.board = Board()

    def run_game(self):
        UserInterface.hello()
        standoff = len(self.board) ** 2
        self.game_mod()
        for user in cycle(self.__users):
            standoff -= 1
            user_step = user.user_step(self.board)
            self.board.set_step(user_step, user)
            print(self.board)
            if self.check_win():
                UserInterface.win_game(user)
                break
            elif not standoff:
                UserInterface.standoff()
                break

    def game_mod(self):
        game_mod = UserInterface.game_mod() - 1
        if game_mod:
            self.__users.extend((User.create_user("x"), User.create_user("o")))
        else:
            self.__users.extend((User.create_user("x"), User.create_bot("o")))


    def check_win(self):
        for itm in zip(self.board, zip(*self.board)):
            for line in itm:
                if line[0] and line.count(line[0]) == len(line):
                    return True
        if self.is_win_line([self.board[idx][idx] for idx in range(0, 3)]):
            return True
        elif self.is_win_line([self.board[line_idx][idx]for line_idx, idx in zip(range(0, 3), range(2, -1, -1))]):
            return True

    @staticmethod
    def is_win_line(line):
        return line[0] and line.count(line[0]) == len(line)

a = Game()
a.run_game()