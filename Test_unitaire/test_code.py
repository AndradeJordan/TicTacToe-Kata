import unittest
from TicTacToeV3.Player_fold import player
from TicTacToeV3.game_strategy import tictactoe,strategy

class TestCode(unittest.TestCase):
    def test_check_if_game_finish_False(self):
        j1 = player.Player("jordan")
        j2 = player.Player("andrade")
        game = tictactoe.TicTac(j1,j2)
        game.player1.ajout_position(1,2)
        game.update_matrix
        self.assertCountEqual(game.check_if_game_finish,(False,0))

    def test_check_if_game_finish_True(self):
        j1 = player.Player("jordan")
        j2 = player.Player("andrade")
        game = tictactoe.TicTac(j1,j2)
        game.player1.ajout_position(1,2)
        game.player1.ajout_position(0,2)
        game.player1.ajout_position(2,2)
        game.update_matrix
        self.assertCountEqual(game.check_if_game_finish,(True,3))

unittest.main(argv=[''], verbosity=2, exit=False)