import time


# 显示平台
class Display:
    def __init__(self, game, show_interval=None):
        self.game = game
        self.show_interval = show_interval
        self.win_player = None
        self.exit = False
        self.step = 1

    def put_piece(self, player, location, done):
        # 子类重写
        if done:
            self.win_player = player

    def mainloop(self):
        while not self.game.play():
            self.step += 1
            if self.show_interval is not None:
                time.sleep(self.show_interval)
        self.show_game_over()

    def show_game_over(self):
        # 子类重写
        if self.win_player is not None:
            print("游戏结束", str(self.win_player) + " 赢了！", "共走步数：", self.step)
        else:
            print("游戏结束", "和局！", "共走步数：", self.step)
