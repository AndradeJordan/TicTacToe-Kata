from Player_fold import player
from game_strategy import tictactoe,strategy



j1 = player.Player("Jordan")
j2 = player.Player("Kevin")
game = tictactoe.TicTac(j1,j2)
strategi_game = strategy.Strategy(game.player1,game.player2,game.matrix)
strategi_game.launch_strategy