import unittest

from solution import maximize_luck_balance


class TestMaximizeLuckBalance(unittest.TestCase):

    def test_case_1(self):
        contests = [(5, 1), (2, 1), (1, 1), (8, 0), (10, 0), (5, 0)]
        k = 3
        self.assertEqual(maximize_luck_balance(contests, k), 29)

    def test_case_2(self):
        contests = [(1, 0)]
        k = 0
        self.assertEqual(maximize_luck_balance(contests, k), 1)

    def test_case_3(self):
        contests = [(3, 0), (7, 0), (2, 0), (9, 0)]
        k = 2
        self.assertEqual(maximize_luck_balance(contests, k), 21)
    
    def test_case_4(self):
        contests = [(3, 1), (7, 1), (2, 1), (9, 1)]
        k = 2
        self.assertEqual(maximize_luck_balance(contests, k), 0)

    def test_case_5(self):
        contests = [(10, 1)]
        k = 0
        self.assertEqual(maximize_luck_balance(contests, k), -10)

    def test_case_6(self):
        contests = [(100, 1), (100, 1), (100, 1), (100, 1), (100, 1)]
        k = 2
        self.assertEqual(maximize_luck_balance(contests, k), -100)

    def test_case_7(self):
        contests = [(8, 1), (4, 0), (5, 1), (3, 1), (7, 0), (9, 1), (2, 0), (10, 0)]
        k = 2
        self.assertEqual(maximize_luck_balance(contests, k), 39)
    
    def test_case_8(self):
        contests = [(i, 1) for i in range(1, 101)] + [(i, 0) for i in range(1, 101)]
        k = 100
        self.assertEqual(maximize_luck_balance(contests, k), -150)

    
if __name__ == "__main__":
    unittest.main()