import time
from .player import Player


# GUI人类玩家
class TkinterHumanPlayer(Player):
    def __init__(self, index, other_index, game):
        super(TkinterHumanPlayer, self).__init__(index, other_index, game)

        self.game.display.canvas.bind("<Button-1>", self.click)
        self.location = None

    def get_next_location(self):
        while True:
            # 等待用户点击
            time.sleep(0.1)
            if self.game.display.exit:
                exit(0)
            if self.location is not None:
                break
        x, y = self.location
        self.location = None
        return x, y

    def click(self, event):
        self.location = self.game.display.parse_location(event.x, event.y)
