import numpy as np
from .player import Player


# 随机玩家
class RandomPlayer(Player):
    def get_next_location(self):
        # 生成随机落子位置
        while True:
            location = np.random.randint(0, self.game.board.width, 2, dtype=np.int8)
            if self.game.board.validate(location):
                return location
