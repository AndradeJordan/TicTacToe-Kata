from .abs_player import absPlayer

class Player(absPlayer):
    def __init__(self,player_name):
        self.player_name = player_name
        self.position = []
        

    @property
    def description(self):
        print( f"This is {self.player_name} player")
        if len(self.position)!=0:
            print("With actually as position :")
            for posi in self.position : 
                print(posi)
        else :
            print("No position actually")
    
    
    def ajout_position(self,i,j):
        self.position.append((i,j))
