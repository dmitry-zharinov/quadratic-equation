import unittest
from modules.quadratic_equation import solve_equation


class SquareRootTestCase(unittest.TestCase):

    def test_first(self):
        result = solve_equation(5, 2, 3)
        self.assertEqual(result, 0)

    def test_no_roots(self):
        result = solve_equation(8, 4, 2)
        # D < 0
        self.assertEqual(result, None)

    def test_root_less_zero(self):
        result = solve_equation(2, 4, 2)
        # D = 0
        self.assertEqual(result, -1)

    def test_a_equal_zero(self):
        self.assertRaises(Exception, solve_equation, 0, 2, 2)
