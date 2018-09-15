import numpy as np
from .player import Player


# 决策玩家
class PolicyPlayer(Player):
    def get_next_location(self):
        max_score = -1
        max_score_i = -1
        max_score_j = -1
        for i, j in self.game.board.available_location:
            score = self.calc_merge_score(i, j)
            if max_score == score:
                if np.random.randint(0, 2, dtype=np.bool_):
                    max_score_i = i
                    max_score_j = j
            elif max_score < score:
                max_score = score
                max_score_i = i
                max_score_j = j
        return max_score_i, max_score_j

    # 综合得分
    def calc_merge_score(self, x, y):
        attack_score = self._calc_attack_score(x, y)
        defense_score = self._calc_defense_score(x, y)
        return attack_score + defense_score * 0.5

    # 防御得分
    def _calc_defense_score(self, x, y):
        return self._calc_x_score(self.other_index, x, y) \
               + self._calc_y_score(self.other_index, x, y) \
               + self._calc_xy_score(self.other_index, x, y) \
               + self._calc_yx_score(self.other_index, x, y)

    # 进攻得分
    def _calc_attack_score(self, x, y):
        return self._calc_x_score(self.index, x, y) \
               + self._calc_y_score(self.index, x, y) \
               + self._calc_xy_score(self.index, x, y) \
               + self._calc_yx_score(self.index, x, y)

    # 横向得分
    def _calc_x_score(self, index, x, y):
        count = 1
        left_space = 0
        right_space = 0
        left_cat = 0
        right_cat = 0
        move_x = x - 1
        while move_x >= 0 and self.game.board.state[move_x, y] == index:
            count += 1
            move_x -= 1
        while move_x >= 0 and self.game.board.state[move_x, y] == 0:
            left_space += 1
            move_x -= 1
        while move_x >= 0 and self.game.board.state[move_x, y] == index:
            left_cat += 1
            move_x -= 1
        move_x = x + 1
        while move_x < self.game.board.width and self.game.board.state[move_x, y] == index:
            count += 1
            move_x += 1
        while move_x < self.game.board.width and self.game.board.state[move_x, y] == 0:
            right_space += 1
            move_x += 1
        while move_x < self.game.board.width and self.game.board.state[move_x, y] == index:
            right_cat += 1
            move_x += 1
        return self._calc_score(count, left_space, right_space, left_cat, right_cat)

    # 竖向得分
    def _calc_y_score(self, index, x, y):
        count = 1
        left_space = 0
        right_space = 0
        left_cat = 0
        right_cat = 0
        move_y = y - 1
        while move_y >= 0 and self.game.board.state[x, move_y] == index:
            count += 1
            move_y -= 1
        while move_y >= 0 and self.game.board.state[x, move_y] == 0:
            left_space += 1
            move_y -= 1
        while move_y >= 0 and self.game.board.state[x, move_y] == index:
            left_cat += 1
            move_y -= 1
        move_y = y + 1
        while move_y < self.game.board.height and self.game.board.state[x, move_y] == index:
            count += 1
            move_y += 1
        while move_y < self.game.board.height and self.game.board.state[x, move_y] == 0:
            right_space += 1
            move_y += 1
        while move_y < self.game.board.height and self.game.board.state[x, move_y] == index:
            right_cat += 1
            move_y += 1
        return self._calc_score(count, left_space, right_space, left_cat, right_cat)

    # 斜向得分
    def _calc_xy_score(self, index, x, y):
        count = 1
        left_space = 0
        right_space = 0
        left_cat = 0
        right_cat = 0
        move_x = x - 1
        move_y = y - 1
        while move_x >= 0 and move_y >= 0 and self.game.board.state[move_x, move_y] == index:
            count += 1
            move_x -= 1
            move_y -= 1
        while move_x >= 0 and move_y >= 0 and self.game.board.state[move_x, move_y] == 0:
            left_space += 1
            move_x -= 1
            move_y -= 1
        while move_x >= 0 and move_y >= 0 and self.game.board.state[move_x, move_y] == index:
            left_cat += 1
            move_x -= 1
            move_y -= 1
        move_x = x + 1
        move_y = y + 1
        while move_x < self.game.board.width and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == index:
            count += 1
            move_x += 1
            move_y += 1
        while move_x < self.game.board.width and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == 0:
            right_space += 1
            move_x += 1
            move_y += 1
        while move_x < self.game.board.width and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == index:
            right_cat += 1
            move_x += 1
            move_y += 1
        return self._calc_score(count, left_space, right_space, left_cat, right_cat)

    # 反斜向得分
    def _calc_yx_score(self, index, x, y):
        count = 1
        left_space = 0
        right_space = 0
        left_cat = 0
        right_cat = 0
        move_x = x - 1
        move_y = y + 1
        while move_x >= 0 and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == index:
            count += 1
            move_x -= 1
            move_y += 1
        while move_x >= 0 and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == 0:
            left_space += 1
            move_x -= 1
            move_y += 1
        while move_x >= 0 and move_y < self.game.board.height and self.game.board.state[move_x, move_y] == index:
            left_cat += 1
            move_x -= 1
            move_y += 1
        move_x = x + 1
        move_y = y - 1
        while move_x < self.game.board.width and move_y >= 0 and self.game.board.state[move_x, move_y] == index:
            count += 1
            move_x += 1
            move_y -= 1
        while move_x < self.game.board.width and move_y >= 0 and self.game.board.state[move_x, move_y] == 0:
            right_space += 1
            move_x += 1
            move_y -= 1
        while move_x < self.game.board.width and move_y >= 0 and self.game.board.state[move_x, move_y] == index:
            right_cat += 1
            move_x += 1
            move_y -= 1
        return self._calc_score(count, left_space, right_space, left_cat, right_cat)

    # 计算得分
    def _calc_score(self, count, left_space, right_space, left_cat, right_cat):
        # 赢了
        if count >= self.game.board.n_in_row:
            return 100000
        elif count == self.game.board.n_in_row - 1:
            # 活4
            if left_space > 0 and right_space > 0:
                return 30000 + (left_space + right_space) * 10 + left_cat + right_cat
            # 半活4
            elif left_space + right_space > 0:
                return 10000 + (left_space + right_space) * 10 + left_cat + right_cat
            else:
                # 死4
                return 0
        elif count == self.game.board.n_in_row - 2:
            # 活3
            if left_space > 0 and right_space > 0:
                return 3000 + (left_space + right_space) * 10 + left_cat + right_cat
            # 半活3
            elif left_space + left_cat >= self.game.board.n_in_row - count or right_space + right_cat >= self.game.board.n_in_row - count:
                return 1000 + (left_space + right_space) * 10 + left_cat + right_cat
            else:
                # 死3
                return 0
        elif count == self.game.board.n_in_row - 3:
            # 活2
            if left_space > 0 and right_space > 0:
                if left_space + right_space >= self.game.board.n_in_row - count:
                    # 活2
                    return 300 + (left_space + right_space) * 10 + left_cat + right_cat
                elif left_cat + right_cat > 0:
                    # 活3
                    return 3000 + (left_space + right_space) * 10 + left_cat + right_cat
                else:
                    # 死2
                    return 0
            # 半活2
            elif left_space > 2 or right_space > 2:
                return 100 + (left_space + right_space) * 10 + left_cat + right_cat
            elif (left_space == 1 and left_cat > 1) or (right_space == 1 and right_cat > 1):
                # 半活4
                return 10000 + (left_space + right_space) * 10 + left_cat + right_cat
            elif (left_space == 2 and left_cat > 0) or (right_space == 2 and right_cat > 0):
                # 半活2
                return 100 + (left_space + right_space) * 10 + left_cat + right_cat
            else:
                # 死2
                return 0
        else:
            return (left_space + right_space) * 10 + left_cat + right_cat
