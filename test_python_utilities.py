__author__ = 'Luis Da Costa'

import unittest
import numpy as np

from python_utilities import prob_choose, idx_of_max

class TestUtilities(unittest.TestCase):

    def setUp(self):
        pass

    def test_proba_choose(self):
        probs = [0.45, 0.35, 0.2]
        # index of maximum value in list:
        max_prob, idx_of_max_prob = idx_of_max(probs)
        # choose from those probabilities several times; the majority should come from the highest:
        indexes = [prob_choose(probs) for _ in range(100)]

        hist, bin_edges = np.histogram(indexes, bins=range(len(probs) + 1))
        _, idx_of_max_in_hist = idx_of_max(hist)
        self.assertTrue(
            idx_of_max_in_hist == idx_of_max_prob,
            "Max probability is %.2f, but it's not chosen more often than others" % (max_prob))
