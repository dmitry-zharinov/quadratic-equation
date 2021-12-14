import unittest

from modules.quadratic import quadratic


class SquareRootTestCase(unittest.TestCase):

    def test_a_equal_zero(self):
        self.assertRaises(Exception, quadratic, 0, 2, 2)

    # D < 0
    def test_no_roots(self):
        result = quadratic(8, 4, 2)
        self.assertEqual(result, None)

    # D = 0
    def test_root_less_zero(self):
        result = quadratic(2, 4, 2)
        self.assertEqual(result, -1)

    # D > 0
    def test_two_roots(self):
        result = quadratic(4, -8, 1)
        self.assertEqual(type(result) is tuple, True)

    def test_c_equal_zero(self):
        result = quadratic(3, -12, 0)
        self.assertEqual(result, (4, 0))
