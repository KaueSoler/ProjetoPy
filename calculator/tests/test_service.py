import unittest
from calculator.service import CalculatorService

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.service = CalculatorService()

    def test_add(self):
        self.assertEqual(self.service.perform_operation('add', 2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.service.perform_operation('subtract', 5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.service.perform_operation('multiply', 2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.service.perform_operation('divide', 6, 3), 2)

    def test_power(self):
        self.assertEqual(self.service.perform_operation('power', 2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(self.service.perform_operation('sqrt', 9), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.service.perform_operation('divide', 1, 0)

if __name__ == '__main__':
    unittest.main()
