import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    # adding a method to test all gutters
    def test_all_gutters(self):
        game = BowlingGame()
        game.throw_many(20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    # adding a perfect method
    def test_perfect_game(self):
        game = BowlingGame()
        game.throw_many(12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    # adding a throw all with 1 pin hit always
    def test_all_ones(self):
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        game.throw_many(number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    #


# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
