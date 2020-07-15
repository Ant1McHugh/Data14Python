from simple_calc import simplecalc
import unittest

class Calctests(unittest.TestCase):
    calc = simplecalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(-4, -5), -9)
        self.assertEqual(self.calc.add(-5, 10), 5)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(-5, 10), -15)
        self.assertIsNotNone(self.calc.subtract(0, 0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(10, 20), 200)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(-5, 10), -50)
        self.assertIsNotNone(self.calc.multiply(0, 0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(10, 20), 0.5)
        self.assertEqual(self.calc.divide(-4, -5), 0.8)
        self.assertEqual(self.calc.divide(-5, 10), -0.5)
        self.assertIsNotNone(self.calc.divide(0, 1))
