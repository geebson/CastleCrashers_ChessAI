
import random

from chess_player import ChessPlayer
from copy import deepcopy

class CastleCrashers_ChessPlayer(ChessPlayer):

    def __init__(self, board, color):
        super().__init__(board, color)

    def get_move(self, your_remaining_time, opp_remaining_time, prog_stuff):
        #basic minimax implementation
        #adjust parameters based on the piece color
        if(self.color=='white'):
            best_score = -10000
            isMazimizing = True
        else:
            best_score = 10000
            isMazimizing = False

        #setup board and moves
        board_copy = deepcopy(self.board)
        possible_moves = board_copy.get_all_available_legal_moves(self.color)
        print(possible_moves)
        return random.choice(
            self.board.get_all_available_legal_moves(self.color))

