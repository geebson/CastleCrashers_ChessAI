import random
from copy import deepcopy

from chess_player import ChessPlayer

class CastleCrashers_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board,color)
        #map a dictionary for all of the piece values
        self.piece_dictionary = {'P': 10,'N': 30,'B': 30,'R': 50,'Q': 90,'K': 10000}
        self.column_array = ['a','b','c','d','e','f','g','h']
        self.row_array = ['1','2','3','4','5','6','7','8']
        
        self.maxDepth = 1
    def evalFunction(self,board):

        white_positions = board.all_occupied_positions('white')
        black_positions = board.all_occupied_positions('black')
        print(black_positions)
        white_evaluation=0
        black_evaluation=0
    #Material Evaluation
        #loop through the pieces for each player, getting the type of pieces and summing their values
        for position in white_positions:
            piece = board[position]
            piece = piece.get_notation().upper()
            if (piece == 'K'): #save the position of the king to use for evaluation later
                king_position_w = position
            value = self.piece_dictionary[piece]
            white_evaluation += value

        for position in black_positions:
            piece = board[position]
            piece = piece.get_notation().upper()
            if (piece == 'K'):
                king_position_b = position
            value = self.piece_dictionary[piece]
            black_evaluation += value
        
    #King's Defense evaluation
        #get the king's positions
        king_row_b = king_position_b[1]
        king_col_b = king_position_b[0]
        king_row_w = king_position_w[1]
        king_col_w = king_position_w[0]
        #get the row below the black king
        defense_row_b = self.row_array[(self.row_array.index(king_row_b))-1]
        #check the 3 spaces around the king in that row
        for i in range(-1,2):
            #make sure it's a possible space on the board before checking
            if self.column_array.index(king_col_b)-i in range(len(self.column_array)):
                defense_col_b = self.column_array[(self.column_array.index(king_col_b))-i]
                #if the space is occupied by a black piece add 1 to black's score
                if (defense_col_b + defense_row_b) in black_positions:
                    black_evaluation += 1

        #follow the same evaluation steps for white's king defense
        defense_row_w = self.row_array[(self.row_array.index(king_row_w))+1]
        for i in range(-1,2):
            if self.column_array.index(king_col_w)-i in range(len(self.column_array)):
                defense_col_w = self.column_array[(self.column_array.index(king_col_w))-i]
                if (defense_col_w + defense_row_w) in white_positions:
                    white_evaluation += 1
    
        score = (white_evaluation - black_evaluation)
        return score

    #alpha beta pruning
    def pruning(self, depth, alpha, beta, isMaximizing):
        value = 0
        #if the depth is 0 or it's a terminal state
        #need to figure out how to check if it's in a terminal state
        if (depth == 0):
            #return the heuristic value
            return value
        #make a copy of the board and get the legal moves
        boardcopy = deepcopy(self.board)
        legal_moves = boardcopy.get_all_available_legal_moves(self.color)
        #if the player is maximizing
        if (isMaximizing):
            #set value to a very low number
            value = -1000000
            #for each legal move
            for x in legal_moves:
                #move = boardcopy.make_move(x[0],x[1])
                value = max(value, self.pruning((depth - 1), alpha, beta, False))
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            #set value to a really high number
            value = 1000000
            for x in legal_moves:
                #move = boardcopy.make_move(x[0],x[1])
                value = min(value, self.pruning((depth - 1), alpha, beta, True))
                if value <= alpha:
                    break
                beta = min(beta, value)
            return value


    def get_move(self,your_remaining_time, opp_remaining_time, prog_stuff):
        #return random.choice(self.board.get_all_available_legal_moves(self.color))
        boardcopy = deepcopy(self.board)
        legal_moves = boardcopy.get_all_available_legal_moves(self.color)
        print(legal_moves)
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
        if (board.is_king_in_checkmate("white")):
            score = -1000000
        elif(board.is_king_in_checkmate("black")):
            score = 1000000

        alpha = 0
        beta = 0
        self.pruning(self.maxDepth, alpha, beta, isMaximizing)

        if (depth == self.maxDepth):
            evaluation = self.evalFunction(board)
            #print(evaluation)
            return evaluation
        
        if(isMaximizing):
            legal_moves = board.get_all_available_legal_moves('black')
            bestScore = -1000000000000  
            for x in legal_moves:
                boardcopy = deepcopy(board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, depth +1 , False)
                bestScore = max(score, bestScore)
            return bestScore           
        else:
            legal_moves = board.get_all_available_legal_moves('white')
            bestScore = 1000000000000
            for x in legal_moves:
                boardcopy = deepcopy(board)
                boardcopy.make_move(x[0],x[1])
                score = self.minimax(boardcopy, depth +1 , True)
                bestScore = min(score, bestScore)
            return bestScore      
            
            
            