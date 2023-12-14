from .abs_TicTac import absTicTac
from .displayer import Displayer
import numpy as np

class TicTac(absTicTac):
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.matrix = np.zeros((3,3))

    @property
    def launch_game(self):
        pass

    @property
    def update_matrix(self):
        position_player1 = self.player1.position
        position_player2 = self.player2.position
        if len(position_player1)!=0:
            for elt in position_player1:
                i,j = elt
                self.matrix[i][j]= 1

        if len(position_player2)!=0:
            for elt in position_player2:
                i,j = elt
                self.matrix[i][j]= -1

    @property
    def check_if_game_finish(self): # if val = -3 player 2 won , if val = +3 player 1 won else the part is not finish 
        tag,val = self.check_if_rows_taken
        if not tag :
            tag,val = self.check_if_cols_taken
        if not tag :
            tag,val = self.check_if_diagonal_taken
        if not tag :
            tag,val = self.check_if_all_fields_taken
                
        Displayer.display_winner(tag,val,self.player1.player_name,self.player2.player_name)
        return tag,val

    @property
    def check_if_rows_taken(self):
        tag,val = False,0
        M = self.matrix
        result_by_rows = M.sum(axis = 1)
        for elt in result_by_rows :
            if elt == 3 :
                tag = True
                return tag, elt
            elif elt == -3 :
                tag = True
                return tag,elt
            else:
                pass

        return tag,val

    @property
    def check_if_cols_taken(self):
        tag,val = False,0
        M = self.matrix
        result_by_rows = M.sum(axis = 0)
        for elt in result_by_rows :
            if elt == 3 :
                tag = True
                return tag, elt
            elif elt == -3 :
                tag = True
                return tag,elt
            else:
                pass
        return tag,val

    @property
    def check_if_diagonal_taken(self):
        tag,val = False,0
        M = self.matrix
                         # left diagonal                            # right diagonal 
        result_by_diagonal = [sum(M[i][i] for i in range(len(M))),sum(M[i][-(i+1)] for i in range(len(M)))]
        for elt in result_by_diagonal :
            if elt == 3 :
                tag = True
                return tag, elt
            elif elt == -3 :
                tag = True
                return tag,elt
            else:
                pass
        return tag,val
    
    @property
    def check_if_all_fields_taken(self):
        tag,val = False,0
        M = self.matrix
        n,m = M.shape
        cp = 0
        for i in range(n):
            for j in range(m):
                if M[i][j] != 0 :
                    cp +=1
        
        if cp == 9 :
            tag = True
            val = cp
            return tag,val
        return tag,val