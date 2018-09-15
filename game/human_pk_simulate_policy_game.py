from .game import Game
from chessboard import ChessBoard
from player.simulate_policy_player import SimulatePolicyPlayer
from player.tkinter_human_player import TkinterHumanPlayer
from display.tkinter_display import TkinterDisplay


# 人类玩家对战模拟策略下棋玩家游戏
class HumanPKSimulatePolicyGame(Game):
    def __init__(self):
        self.board = ChessBoard()
        self.display = TkinterDisplay(self)
        self.player1 = TkinterHumanPlayer(1, 2, self)
        self.player2 = SimulatePolicyPlayer(2, 1, self)

        super(HumanPKSimulatePolicyGame, self).__init__(self.board, self.display, self.player1, self.player2)
