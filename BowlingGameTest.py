import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    # adding a test method to test all gutters
    def test_all_gutters(self):
        """
        @:parameter 20 times throw
        @:parameter 0 pins hit
        @:returns 0 score
        """
        game = BowlingGame()
        game.throw_many(20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    # adding a test method to test a perfect game
    def test_perfect_game(self):
        """
        @:parameter 12 times throw
        @:parameter 10 pins hit
        @:returns 300 score
        """
        game = BowlingGame()
        game.throw_many(12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)

    # adding a test method for throw all with 1 pin hit always
    def test_all_ones(self):
        """
        @:parameter 20 times throw
        @:parameter 1 pins hit
        @:returns 20 score
        """
        game = BowlingGame()
        number_of_times = 20
        pins = 1
        game.throw_many(number_of_times, pins)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    # adding a test method for different types of throws
    def test_different_throws(self):
        """
        @:parameter 5 times single throw
        @:parameter different numbers of pins hit
        @:returns 15 score
        """
        game = BowlingGame()
        game.throw_one(6)
        game.throw_one(0)
        game.throw_one(7)
        game.throw_one(0)
        game.throw_one(2)
        for _ in range(15):
            game.throw_one(0)
        game.calculate_score()
        self.assertEqual(game.score, 15)

    # adding a test method for what is meant to be a spare
    def test_for_spare(self):
        """
        @:parameter 4 times single throw spare
        @:parameter different number of pins hit
        @:returns 24 score
        """
        game = BowlingGame()
        game.throw_one(4)
        game.throw_one(6)
        game.throw_one(7)
        game.throw_one(0)
        for _ in range(16):
            game.throw_one(0)
        game.calculate_score()
        self.assertEqual(game.score, 24)

    # adding test method to test the strike
    def test_for_strike(self):
        """
        @:parameter 3 times throw including strike
        @:parameter different number of pins hit
        @:returns 22 score
        """
        game = BowlingGame()
        game.throw_one(10)
        game.throw_one(4)
        game.throw_one(2)
        game.throw_many(17, 0)
        game.calculate_score()
        self.assertEqual(game.score, 22)


# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
