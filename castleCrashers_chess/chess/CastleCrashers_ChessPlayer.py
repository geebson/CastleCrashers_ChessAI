import random
from copy import deepcopy

from chess_player import ChessPlayer

class CastleCrashers_ChessPlayer(ChessPlayer):
    def __init__(self, board, color):
        super().__init__(board,color)
        #map a dictionary for all of the piece values
        self.piece_dictionary = {'P': 1,'N': 3,'B': 3,'R': 5,'Q': 9,'K': 10000}
        self.column_array = ['a','b','c','d','e','f','g','h']
        self.row_array = ['1','2','3','4','5','6','7','8']
        
        self.maxDepth = 1
    def evalFunction(self,board):
        #some kind of rating system for each piece
        white_positions = board.all_occupied_positions('white')
        black_positions = board.all_occupied_positions('black')
        print(black_positions)
        white_evaluation=0
        black_evaluation=0
        #loop through the piece positions for each player, getting the piece type and summing the corresponding values
        for position in white_positions:
            piece = board[position]
            piece = piece.get_notation().upper()
            #save the position of the king to use for evaluation later
            if (piece == 'K'):
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
        score = (white_evaluation - black_evaluation)
        #print('King position white: ', king_position_w)
        print('King position black: ', king_position_b)
        #check the three spaces below the black king and three spaces above the white king
        #get the row and column of both kings
        king_row_b = king_position_b[1]
        king_col_b = king_position_b[0]
        king_row_w = king_position_w[1]
        king_col_w = king_position_w[0]
        #check where the column is
        #check where the row is
        defense_row_b = self.row_array[(self.row_array.index(king_row_b))-1]
        for i in range(-1,2):
            defense_col_b = self.column_array[(self.column_array.index(king_col_b))-i]
            print(defense_col_b)
            if (defense_col_b + defense_row_b) in black_positions:
                print(defense_col_b,defense_row_b, ' occupied')
        return score
    
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
        legal_moves = board.get_all_available_legal_moves(self.color)
        if (board.is_king_in_checkmate("white")):
            score = -1000000
        elif(board.is_king_in_checkmate("black")):
            score = 1000000
        
        if (depth == self.maxDepth):
            evaluation = self.evalFunction(board)
            #print(evaluation)
            return evaluation
        
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
            
            
            