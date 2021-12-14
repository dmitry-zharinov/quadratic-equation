import unittest

from modules.quadratic import quadratic


class SquareRootTestCase(unittest.TestCase):

    # a = 0
    def test_not_quadratic(self):
        self.assertRaises(Exception, quadratic, 0, 2, 2)

    # D < 0
    def test_no_roots(self):
        result = quadratic(8, 4, 2)
        self.assertEqual(result, None)

    # D = 0
    def test_one_root(self):
        result = quadratic(2, 4, 2)
        self.assertEqual(result, -1)

    # D > 0
    def test_two_roots(self):
        result = quadratic(4, -8, 1)
        self.assertEqual(type(result) is tuple, True)

    def test_c_equal_zero(self):
        result = quadratic(3, -12, 0)
        self.assertEqual(result, (4, 0))

    def test_real_roots(self):
         result = quadratic(5, 5, 1)
         self.assertAlmostEqual(result[0], -0.2763932)
         self.assertAlmostEqual(result[1], -0.723606797)
