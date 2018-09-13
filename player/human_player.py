from .player import Player


# 人类玩家
class HumanPlayer(Player):
    def get_next_location(self):
        while True:
            location = input("Your move: ")
            try:
                if isinstance(location, str):
                    location = [int(n, 10) for n in location.split(",")]
                if self.game.board.validate(location):
                    return location
            except:
                pass
            print("illegal move, input again, example: 1,2")
