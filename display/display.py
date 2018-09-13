# 显示平台
class Display:
    def __init__(self, game, show_interval=0.001):
        self.game = game
        self.show_interval = show_interval
        self.win_player = None
        self.exit = False

    def put_piece(self, player, location, done):
        # 子类重写
        if done:
            self.win_player = player

    def mainloop(self):
        # 子类重写
        while not self.game.play():
            pass
