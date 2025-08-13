# tests/test_calculator.py
import unittest
from src.calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(-2, -1), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(6, 3), 3)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(7, 5), 2)

if __name__ == '__main__':
    unittest.main()