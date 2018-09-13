from game.policy_pk_policy_game import PolicyPKPolicyGame
from game.human_pk_policy_game import HumanPKPolicyGame
from game.game import Game
from chessboard import ChessBoard
from display.tkinter_display import TkinterDisplay
from display.print_display import PrintDisplay
from player.random_player import RandomPlayer
from player.human_player import HumanPlayer
from player.policy_player import PolicyPlayer
from player.tkinter_human_player import TkinterHumanPlayer


# 测试策略玩家自我对弈一局耗时
def policy_pk_policy_time_cost():
    import time

    start = time.clock()
    PolicyPKPolicyGame().mainloop()
    print("策略自我对弈一局耗时: ", time.clock() - start)


# 人机对战
def human_pk_policy():
    HumanPKPolicyGame().mainloop()


# 自定义游戏，选择显示平台和玩家
def custom_game():
    # 策略玩家自我对弈的动态效果
    board = ChessBoard()
    game = Game(board, None, None, None)
    display = TkinterDisplay(game, 1)
    player1 = PolicyPlayer(1, 2, game)
    player2 = PolicyPlayer(2, 1, game)
    game.display = display
    game.player = game.player1 = player1
    game.player2 = player2
    game.mainloop()


# 游戏入口
if __name__ == "__main__":
    # custom_game()
    # policy_pk_policy_time_cost()
    human_pk_policy()
