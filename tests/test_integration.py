import unittest
from src.calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_add_and_multiply(self):
        calc = Calculator()
        result = calc.multiply(calc.add(2, 3), 10)
        self.assertEqual(result, 50)
