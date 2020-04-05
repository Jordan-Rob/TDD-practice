import unittest

import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(2, 8)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = calc.subtract(9, 7)
        self.assertEqual(result, 2)

    def test_divide(self):
        self.assertEqual(calc.divide(16, 8), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 3), 6)

    def test_trueOrFalse(self):
        self.assertTrue(calc.greater(7, 5))

    def test_subtract(self):
        self.assertRaises(ValueError, calc.subtract, 10, 18)


if __name__ == "__main__":
    unittest.main()
