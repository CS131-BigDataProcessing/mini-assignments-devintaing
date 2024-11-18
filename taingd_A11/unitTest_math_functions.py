import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):
  def test_divide(self):
    self.assertEqual(divide(10, 4), 2.5)
    self.assertEqual(divide(10, 2), 5)
    self.assertEqual(divide(10, 0), "You cannot divide by 0.")
    self.assertEqual(divide(0, 2), 0)
    self.assertEqual(divide(-10, 2), -5)
    self.assertEqual(divide(10, -2), -5)
    self.assertEqual(divide(-10, -2), 5)
    self.assertEqual(divide(0, 0), "You cannot divide by 0.")
    self.assertEqual(divide(-10, 0), "You cannot divide by 0.")

  def test_power(self):
    self.assertEqual(power(2, 3), 8)
    self.assertEqual(power(5, 0), 1)
    self.assertEqual(power(4, -3), 0.015625)
    self.assertEqual(power(-4, 3), -64)
    self.assertEqual(power(0, 3), 0)
    self.assertEqual(power(2, 0.5), 1.4142135623730951)
    self.assertEqual(power(0.5, 2), 0.25)
    self.assertEqual(power(0.5, -2), 4)
    self.assertEqual(power(-0.5, -2), 4)

if __name__ == '__main__':
  unittest.main()
