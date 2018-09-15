from utils.top_n import TopN
from chessboard import ChessBoard
from game.game import Game
from display.display import Display
from .policy_player import PolicyPlayer


# 模拟策略下棋玩家
class SimulatePolicyPlayer(PolicyPlayer):
    def __init__(self, index, other_index, game, max_breadth=10, max_depth=10):
        super(SimulatePolicyPlayer, self).__init__(index, other_index, game)
        self.max_breadth = max_breadth
        self.max_depth = max_depth

    def get_next_location(self):
        # 从[max_breadth]中最优走法中依次模拟下完，直到赢得比赛，若没有赢则去分数最高的下法
        top = self._get_top_location()
        n = 0
        for _, x, y in top:
            state = self.game.board.state.copy()
            state[x, y] = self.index
            n += 1
            if self._simulate_play(state):
                print("模拟次数：", n)
                return x, y
        _, x, y = top[0]
        print("模拟次数：", n)
        return x, y

    # 获取分数最高的前[max_breadth]种走法
    def _get_top_location(self):
        top_n = TopN(self.max_breadth, lambda item: item[0], lambda a, b: a[0] - b[0])
        for i, j in self.game.board.available_location:
            score = self.calc_merge_score(i, j)
            top_n.push((score, i, j))
        return top_n.top

    # 模拟下棋
    def _simulate_play(self, state):
        board = ChessBoard(self.game.board.width, self.game.board.height, self.game.board.n_in_row, state)
        game = Game(board, None, None, None)
        display = Display(game)
        player1 = PolicyPlayer(self.other_index, self.index, game)
        player2 = PolicyPlayer(self.index, self.other_index, game)
        game.display = display
        game.player = game.player1 = player1
        game.player2 = player2
        game.mainloop()
        return display.win_player is not None and display.win_player.index == self.index
