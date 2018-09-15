import numpy as np
from .player import Player


# 随机玩家
class RandomPlayer(Player):
    def get_next_location(self):
        # 生成随机落子位置
        return self.game.board.available_location[np.random.randint(0, len(self.game.board.available_location))]
