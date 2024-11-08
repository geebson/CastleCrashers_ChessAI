import random
from copy import deepcopy

from chess_player import ChessPlayer

class CastleCrashers_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board,color)
    
        self.maxDepth = 1
    def evalFunction(self,board):
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
            
            
            