


# 游戏
class Game:
    def __init__(self, board, display, player1, player2):
        self.board = board
        self.display = display
        self.player1 = player1
        self.player2 = player2
        self.player = self.player1

    def mainloop(self):
        self.display.mainloop()

    def play(self):
        if self.board.is_full():
            return True
        if self.player.put_piece():
            return True

        if self.player == self.player1:
            self.player = self.player2
        else:
            self.player = self.player1
        return False
