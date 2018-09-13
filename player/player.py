# 玩家
class Player:
    def __init__(self, index, other_index, game):
        self.index = index
        self.other_index = other_index
        self.game = game

    def __str__(self):
        return self.__class__.__name__ + str(self.index)

    # 落子
    def put_piece(self):
        location = self.get_next_location()
        done = self.game.board.put_piece(self, location)
        self.game.display.put_piece(self, location, done)
        return done

    # 获取下一步的落子位置
    def get_next_location(self):
        # 子类重写
        pass
