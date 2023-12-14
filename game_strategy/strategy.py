from .tictactoe import TicTac
from .displayer import Displayer
from Player_fold.player import Player

class Strategy(TicTac):
    def __init__(self,player1,player2,matrix):
        super().__init__(player1,player2)
        self.matrix = matrix

    def choose_element(self,number): ## séparer les nack end et front end   tous les print dans le displayer , gérer les returns 
        Displayer.display_player_turn(number,self.player1.player_name,self.player2.player_name)
        tag = False
        M = self.matrix
        while tag == False:
            i, j = Displayer.get_player_items()
            if not i in (0,1,2) and not j in (0,1,2):
                Displayer.message_player_items(0)
            elif M[i][j]==0:
                tag = True
                Displayer.message_player_items(1)
            else :
                Displayer.message_player_items(2)
        return i, j 

    @property
    def launch_strategy(self):
        Displayer.display_turn()
        Displayer.display_field(self)
        tag,val = self.check_if_game_finish
        while tag == False :
            i_player1,j_player1 = self.choose_element(1)
            self.player1.ajout_position(i_player1,j_player1)
            self.update_matrix
            Displayer.display_field(self)
            tag,val = self.check_if_game_finish
            if tag :
                self.re_launch_strategy
            i_player2,j_player2 = self.choose_element(2)
            self.player2.ajout_position(i_player2,j_player2)
            self.update_matrix
            Displayer.display_turn()
            Displayer.display_field(self)
            tag,val = self.check_if_game_finish

        self.re_launch_strategy

    @property
    def re_launch_strategy(self):
        
        val = Displayer.get_val_restart()
        if val == 1 : 
            j1 = Player(self.player1.player_name)
            j2 = Player(self.player2.player_name)
            game = TicTac(j1,j2)
            strategi_game = Strategy(game.player1,game.player2,game.matrix)
            strategi_game.launch_strategy
        
            