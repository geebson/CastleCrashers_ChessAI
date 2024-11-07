
import random

from chess_player import ChessPlayer

class Random_ChessPlayer(ChessPlayer):

    def __init__(self, board, color):
        super().__init__(board, color)

    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        return random.choice(
            self.board.get_all_available_legal_moves(self.color))

