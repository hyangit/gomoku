import time
from .display import Display


# 打印机显示平台
class PrintDisplay(Display):
    def __init__(self, game, show_interval=None):
        super(PrintDisplay, self).__init__(game, show_interval)
        print("---" * self.game.board.width)

    def put_piece(self, player, location, done):
        super(PrintDisplay, self).put_piece(player, location, done)

        print("---" * self.game.board.width)
        print(self.game.board.state)
