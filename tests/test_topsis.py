import os
import sys
import unittest

sys.path.insert(0, 'D:/topsis_package/topsis')
from topsis import topsis

class TestTopsis(unittest.TestCase):
    def test_topsis(self):
        decision_matrix = [
            [250, 16, 12, 5],
            [200, 16, 8, 3],
            [300, 32, 16, 4],
            [275, 8, 8, 4],
            [225, 16, 16, 2]
        ]
        weights = [0.25, 0.25, 0.25, 0.25]
        impacts = ['+', '+', '-', '+']
        rankings, scores = topsis(decision_matrix, weights, impacts)
        self.assertEqual(list(rankings), [3, 1, 2, 4, 5])

if __name__ == '__main__':
    unittest.main()
