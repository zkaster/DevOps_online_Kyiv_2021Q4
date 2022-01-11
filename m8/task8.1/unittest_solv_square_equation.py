import unittest
import solv_square_equation

class Solv_Sq_Eq (unittest.TestCase):
    def test_validate_param(self):
        self.assertEqual(solv_square_equation.validate_param(1), True)

    def test_discriminant (self):
        self.assertEqual(solv_square_equation.discriminant(1, 4, 4),0)

    def test_roots (self):
        self.assertListEqual(solv_square_equation.roots(0, 1, 4),[-2,-2])

    def test_solv_square (self):
        self.assertEqual(solv_square_equation.solv_square(1, 4, 4),True)
