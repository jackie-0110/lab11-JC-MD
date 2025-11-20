#https://github.com/jackie-0110/lab11-JC-MD
import unittest
import calculator
import math
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1,2), 3)
        self.assertEqual(calculator.add(2,3), 5)
        self.assertEqual(calculator.add(3,4), 7)
    def test_subtract(self):
        self.assertEqual(calculator.add(1,2), -1)
        self.assertEqual(calculator.add(2,3), -1)
        self.assertEqual(calculator.add(3,4), -1)
    def test_multiply(self):
        self.assertEqual(calculator.mul(1,2), 2)
        self.assertEqual(calculator.mul(3,4), 12)
        self.assertEqual(calculator.mul(5,6), 30)
        self.assertEqual(calculator.mul(-2,-5), 10)
        self.assertEqual(calculator.mul(-2,5), -10)
        self.assertEqual(calculator.mul(0,10), 0)
    def test_divide(self):
        self.assertAlmostEqual(calculator.div(10, 2), 5.0)
        self.assertAlmostEqual(calculator.div(7, 2), 3.5)
        self.assertAlmostEqual(calculator.div(15, 3), 5.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(1, 0)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10,0)
    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3,4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5,12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(7,24), 25.0)
        self.assertAlmostEqual(calculator.hypotenuse(9,40), 41.0)
    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(4), 2.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(25), 5.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
if __name__ == "__main__":
    unittest.main()

