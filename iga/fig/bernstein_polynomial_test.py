"""
This module is a unit test of the bernstein_polynomial implementation.

To run
$ python bernstein_polynomial_test.py              # terse interaction
$ python -m unittest bernstein_polynomial_test     # default interaction
$ python -m unittest -v bernstein_polynomial_test  # verbose interaction

"""
# standard library imports
import sys
# 
import numpy as np
from unittest import TestCase, main
# 
import bernstein_polynomial as bp

class TestBernstein(TestCase):

    @classmethod
    def setUpClass(cls):
        cls._TOL = 1e-6  # tolerance
        cls._nti = 4  # number of time intervals
        # t, e.g., four intervals, five evaluation points
        cls._t = np.linspace(0, 1, cls._nti+1)

    @classmethod
    def same(cls, a, b):
        same_to_tolerance = False
        print(f'array a = {a}')
        print(f'array b = {b}')

        l2norm_diff = np.linalg.norm(a - b)
        print(f'l2norm_diff = {l2norm_diff}')

        if np.abs(l2norm_diff) < cls._TOL:
            same_to_tolerance = True

        return same_to_tolerance


    def test_b01(self):
        # nti = 4
        # t = np.linspace(0, 1, self._nti+1)  # four intervals, five evaluation points
        known = 1 - self._t
        i, p = 0, 1
        calc = bp.bernstein_polynomial(i, p, self._nti)
        self.assertTrue(self.same(known, calc))

    def test_b11(self):
        # nti = 4
        # t = np.linspace(0, 1, self._nti+1)  # four intervals, five evaluation points
        known = self._t
        i, p = 1, 1
        calc = bp.bernstein_polynomial(i, p, self._nti)
        self.assertTrue(self.same(known, calc))


if __name__ == '__main__':
    main()  # calls unittest.main()
