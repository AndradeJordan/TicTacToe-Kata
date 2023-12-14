class Displayer :
    Compteur = 1
    @staticmethod
    def display_field(game): #
        n, m = game.matrix.shape
        M = game.matrix
        for i in range(n):
            tmp_list =["*","*","*"]
            for j in range(m):
                if M[i][j] == 1:
                    tmp_list[j] = "X"
                elif M[i][j] == -1 :
                    tmp_list[j] = "O"
            print(*tmp_list)
            tmp_list =["*","*","*"]
        Displayer.Compteur = Displayer.Compteur//2 + 1

    @staticmethod
    def display_turn():
        print("Turn number : ",Displayer.Compteur)

    @staticmethod
    def display_player_turn(number,name1,name2):
        if number == 1 :
            print(f"****************** Player "+name1+" turn ******************")
        else :
            print(f"****************** Player "+name2+" turn ******************")
    
    @staticmethod
    def get_player_items():
        i = int(input("***** Which item's rows ? "))
        j = int(input("***** Which item's cols ? "))
        return i,j
    
    @staticmethod
    def message_player_items(num):
        if num == 0:
            print("---- > Sorry you have to choose in (0,1,2) !!")
        elif num == 1:
            print("---- > Item Validated ")
        else :
            print("----> Sorry this item is already taken !!")
    
    @staticmethod
    def get_val_restart():
        while True:
            user_val = input("Would you like to recommit a game ? Tap 1 : yes or 0 : no ")
            try:
                number = int(user_val)
                break  
            except ValueError:
                print(" !!!!  Please enter a valid integer ( 0 or 1 ) !!!!!")
        if number == 0 :
            print("*****   Thank you   *****")
            exit()
        return number

    @staticmethod
    def display_winner(tag,val,name1,name2):
        if tag == True :
            print(" *-*-*-*-*-* Game is Over !!!! *-*-*-*-*--*")
            if val == -3 :
                print("^^^^^^^ Congratulations The winner is ",name2,)
            elif val == 3 :
                print("^^^^^^^ Congratulations The winner is ",name1,)
            else :
                print("^^^^^^^^ All the fields are taken ! ^^^^^^")
            
        else :
            pass