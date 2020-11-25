import unittest
from Bowling import BowlingGame


class BowlingGameTests(unittest.TestCase):
    # creating a global variable for avoiding repetition of code
    game = BowlingGame()

    # creating static method for many throws
    @staticmethod
    def throw_many(game, number_of_times, pins):
        for _ in range(number_of_times):
            game.throw(pins)


# calling all tests in this class to be executed
if __name__ == '__main__':
    unittest.main()
