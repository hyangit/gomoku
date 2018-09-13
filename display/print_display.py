import time
from .display import Display


# 打印机显示平台
class PrintDisplay(Display):
    def __init__(self, game, show_interval=0.001):
        super(PrintDisplay, self).__init__(game, show_interval)
        print("---" * self.game.board.width)

    def put_piece(self, player, location, done):
        super(PrintDisplay, self).put_piece(player, location, done)

        print("---" * self.game.board.width)
        print(self.game.board.state)

    def mainloop(self):
        while not self.game.play():
            time.sleep(self.show_interval)
        self.show_game_over()

    def show_game_over(self):
        if self.win_player is not None:
            print(str(self.win_player) + " 赢了！")
        else:
            print("和局！")
