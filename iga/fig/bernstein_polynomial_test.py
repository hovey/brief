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
        nti = 4
        t = np.linspace(0, 1, nti+1)  # four intervals, five evaluation points
        b01_known = 1 - t
        print(f'b01_known = {b01_known}')
        i = 0
        p = 1
        b01_calc = bp.bernstein_polynomial(i, p, nti)
        print(f'b01_cals = {b01_calc}')
        l2norm_diff = np.linalg.norm(b01_known - b01_calc)
        print(f'l2norm_diff = {l2norm_diff}')
        self.assertTrue(self.same(b01_calc, b01_known))

    # def same(self, a, b):
    #     same_to_tolerance = False
    #     print(f'array a = {a}')
    #     print(f'array b = {b}')

    #     l2norm_diff = np.linalg.norm(a - b)
    #     print(f'l2norm_diff = {l2norm_diff}')

    #     if np.abs(l2norm_diff) < self._tol:
    #         same_to_tolerance = True

    #     return same_to_tolerance

if __name__ == '__main__':
    main()  # calls unittest.main()
