import unittest
from unittest.mock import patch
from calculator.view import CalculatorView

class TestCalculatorView(unittest.TestCase):
    @patch('builtins.input', side_effect=['add', '2', '3'])
    def test_get_user_input(self, mock_input):
        view = CalculatorView()
        operation, a, b = view.get_user_input()
        self.assertEqual(operation, 'add')
        self.assertEqual(a, 2.0)
        self.assertEqual(b, 3.0)

    @patch('builtins.print')
    def test_display_result(self, mock_print):
        view = CalculatorView()
        view.display_result(10)
        mock_print.assert_called_with("Result: 10")

    @patch('builtins.print')
    def test_display_error(self, mock_print):
        view = CalculatorView()
        view.display_error("Test error")
        mock_print.assert_called_with("Error: Test error")

if __name__ == '__main__':
    unittest.main()
