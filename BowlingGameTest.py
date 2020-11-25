import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    game = BowlingGame()

    def throw_many(self, pins, number_of_times):
        for _ in range(number_of_times):
            self.game.throw(pins)

    def test_all_gutters(self):
        self.throw_many(20, 0)
        self.game.calculate_score()
        self.assertEquals(0, self.game.score())

    # def test_perfect_game(self):
    #     game = BowlingGame()
    #     self.throw_many(game, 12, 10)
    #     game.calculate_score()
    #     self.assertEquals(game.score, 300)
    #
    # def test_all_ones(self):
    #     game = BowlingGame()
    #     number_of_times = 20
    #     pins = 1
    #     self.throw_many(game, number_of_times, pins)
    #     game.calculate_score()
    #     self.assertEquals(game.score, 20)
    #
    # def test_different_throws(self):
    #     game = BowlingGame()
    #     game.throw(6)
    #     game.throw(0)
    #     game.throw(7)
    #     game.throw(0)
    #     game.throw(2)
    #     for _ in range(15):
    #         game.throw(0)
    #     game.calculate_score()
    #     self.assertEquals(game.score, 15)
    #
    # def test_for_spare(self):
    #     game = BowlingGame()
    #     game.throw(4)
    #     game.throw(6)
    #     game.throw(7)
    #     game.throw(0)
    #     for _ in range(16):
    #         game.throw(0)
    #     game.calculate_score()
    #     self.assertEquals(game.score, 24)
    #
    # def test_for_strike(self):
    #     game = BowlingGame()
    #     game.throw(10)
    #     game.throw(4)
    #     game.throw(2)
    #     self.throw_many(game, 17, 0)
    #     game.calculate_score()
    #     self.assertEquals(game.score, 22)
    #

if __name__ == '__main__':
    unittest.main()
