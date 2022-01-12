import unittest
import solv_square_equation


class TestSquareEquation(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(solv_square_equation.discriminant(4, -2, 22), -348)
        self.assertEqual(solv_square_equation.discriminant(1, 2, 1), 0)
        self.assertEqual(solv_square_equation.discriminant(-1, -2, 8), 36)

    def test_roots(self):
        self.assertEqual(solv_square_equation.roots(-348, 4, -2, 22), None)
        self.assertEqual(solv_square_equation.roots(0, 1, 2, 1), -1)
        self.assertEqual(solv_square_equation.roots(36, -1, -2, 8), (-4, 2))

    def test_solv_square(self):
        self.assertEqual(solv_square_equation.solv_square(4, -2, 22), None)
        self.assertEqual(solv_square_equation.solv_square(1, 2, 1), -1)
        self.assertEqual(solv_square_equation.solv_square(-1, -2, 8), (-4, 2))


if __name__ == '__main__':
    unittest.main()
