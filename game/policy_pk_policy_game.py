from .game import Game
from chessboard import ChessBoard
from player.policy_player import PolicyPlayer
from display.display import Display


# 策略玩家对战策略玩家游戏
class PolicyPKPolicyGame(Game):
    def __init__(self):
        self.board = ChessBoard()
        self.display = Display(self)
        self.player1 = PolicyPlayer(1, 2, self)
        self.player2 = PolicyPlayer(2, 1, self)

        super(PolicyPKPolicyGame, self).__init__(self.board, self.display, self.player1, self.player2)
