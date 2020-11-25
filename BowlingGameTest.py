import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):

    # adding a method to test all gutters
    def test_all_gutters(self):
        game = BowlingGame()
        game.throw_many(20, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)


# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
