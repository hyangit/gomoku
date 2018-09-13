from .game import Game
from chessboard import ChessBoard
from player.tkinter_human_player import TkinterHumanPlayer
from player.policy_player import PolicyPlayer
from display.tkinter_display import TkinterDisplay


# 人类玩家对战策略玩家游戏
class HumanPKPolicyGame(Game):
    def __init__(self):
        self.board = ChessBoard()
        self.display = TkinterDisplay(self)
        self.player1 = TkinterHumanPlayer(1, 2, self)
        self.player2 = PolicyPlayer(2, 1, self)

        super(HumanPKPolicyGame, self).__init__(self.board, self.display, self.player1, self.player2)
