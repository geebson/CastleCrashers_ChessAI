import random
from copy import deepcopy

from chess_player import ChessPlayer

class CastleCrashers_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board,color)
        #map a dictionary for all of the piece values
        self.piece_dictionary = {'P': 1,'N': 3,'B': 3,'R': 5,'Q': 9,'K': 10000}
        
        self.maxDepth = 1
    def evalFunction(self,board):
        #some kind of rating system for each piece
        #put all of the white pieces in one array
        white_positions = board.all_occupied_positions('white')
        black_positions = board.all_occupied_positions('black')
        white_evaluation=0
        black_evaluation=0
        for position in white_positions:
            piece = board[position]
            piece = piece.get_notation().upper()
            value = self.piece_dictionary[piece]
            white_evaluation += value
        for position in black_positions:
            piece = board[position]
            piece = piece.get_notation().upper()
            value = self.piece_dictionary[piece]
            black_evaluation += value
        #put all of the black pieces in another array
        #black_positions = self.all_occupied_positions('black')
        #loop through both and sum the values of the pieces
        #score = white pieces - black pieces
        return 0
    
    def get_move(self,your_remaining_time, opp_remaining_time, prog_stuff):
        #return random.choice(self.board.get_all_available_legal_moves(self.color))
        boardcopy = deepcopy(self.board)
        legal_moves = boardcopy.get_all_available_legal_moves(self.color)
        
        if(self.color == 'white'):
      
            bestscore = -1000000000000
            for x in legal_moves:
                boardcopy = deepcopy(self.board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, 0,True)
                if (score > bestscore):
                    bestscore = score
                    bestMove = x
            return bestMove            
        elif (self.color == 'black'):
            bestscore = 1000000000000
            for x in legal_moves:
                boardcopy = deepcopy(self.board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, 0,False)
                if (score < bestscore):
                    bestscore = score
                    bestMove = x
            return bestMove            
                
    def minimax(self, board, depth, isMaximizing):
        legal_moves = board.get_all_available_legal_moves(self.color)
        if (board.is_king_in_checkmate("white")):
            score = -1000000
        elif(board.is_king_in_checkmate("black")):
            score = 1000000
        
        if (depth == self.maxDepth):
            return self.evalFunction(board)
        
        if(isMaximizing):
            bestScore = -1000000000000  
            for x in legal_moves:
                boardcopy = deepcopy(board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, depth +1 , False)
                bestScore = max(score, bestScore)
            return bestScore           
        else:
            bestScore = 1000000000000
            for x in legal_moves:
                boardcopy = deepcopy(board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, depth +1 , True)
                bestScore = min(score, bestScore)
            return bestScore      
            
            
            