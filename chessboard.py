import numpy as np


# 棋谱
class ChessBoard:
    def __init__(self, width=15, height=15, n_in_row=5, state=None):
        self.width = width
        self.height = height
        self.n_in_row = n_in_row
        self.state = state
        if state is None:
            self.state = np.zeros([width, height], dtype=np.byte)

    # 落子，返回 是否结束
    def put_piece(self, player, location):
        if not self.validate(location):
            raise Exception("location error")
        x, y = location
        self.state[x, y] = player.index
        return self._is_done(player, x, y)

    # 是否可以落子
    def validate(self, location):
        if len(location) != 2:
            return False
        x, y = location
        return 0 <= x < self.width and 0 <= y < self.height and self.state[x, y] == 0

    # 棋盘已满
    def is_full(self):
        return self.state.all()

    # 是否结束
    def _is_done(self, player, x, y):
        return self._x_is_done(player, x, y) or self._y_is_done(player, x, y) or self._xy_is_done(player, x, y) or self._yx_is_done(player, x, y)

    # 横向是否结束
    def _x_is_done(self, player, x, y):
        count = 1
        move_x = x - 1
        while move_x >= 0 and self.state[move_x, y] == player.index:
            count += 1
            move_x -= 1
        move_x = x + 1
        while move_x < self.width and self.state[move_x, y] == player.index:
            count += 1
            move_x += 1
        return count >= self.n_in_row

    # 竖向是否结束
    def _y_is_done(self, player, x, y):
        count = 1
        move_y = y - 1
        while move_y >= 0 and self.state[x, move_y] == player.index:
            count += 1
            move_y -= 1
        move_y = y + 1
        while move_y < self.height and self.state[x, move_y] == player.index:
            count += 1
            move_y += 1
        return count >= self.n_in_row

    # 斜向是否结束
    def _xy_is_done(self, player, x, y):
        count = 1
        move_x = x - 1
        move_y = y - 1
        while move_x >= 0 and move_y >= 0 and self.state[move_x, move_y] == player.index:
            count += 1
            move_x -= 1
            move_y -= 1
        move_x = x + 1
        move_y = y + 1
        while move_x < self.width and move_y < self.height and self.state[move_x, move_y] == player.index:
            count += 1
            move_x += 1
            move_y += 1
        return count >= self.n_in_row

    # 反斜向是否结束
    def _yx_is_done(self, player, x, y):
        count = 1
        move_x = x - 1
        move_y = y + 1
        while move_x >= 0 and move_y < self.height and self.state[move_x, move_y] == player.index:
            count += 1
            move_x -= 1
            move_y += 1
        move_x = x + 1
        move_y = y - 1
        while move_x < self.width and move_y >= 0 and self.state[move_x, move_y] == player.index:
            count += 1
            move_x += 1
            move_y -= 1
        return count >= self.n_in_row
