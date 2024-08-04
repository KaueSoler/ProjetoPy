import unittest
from unittest.mock import patch, MagicMock
from calculator.controller import CalculatorController

class TestCalculatorController(unittest.TestCase):
    @patch('calculator.controller.CalculatorView')
    @patch('calculator.controller.CalculatorService')
    def setUp(self, MockService, MockView):
        self.mock_service = MockService.return_value
        self.mock_view = MockView.return_value
        self.controller = CalculatorController()

    def test_run_success(self):
        self.mock_view.get_user_input.return_value = ('add', 2, 3)
        self.mock_service.perform_operation.return_value = 5
        with patch('builtins.print') as mocked_print:
            self.controller.run()
            mocked_print.assert_called_with("Result: 5")

    def test_run_error(self):
        self.mock_view.get_user_input.return_value = ('divide', 1, 0)
        self.mock_service.perform_operation.side_effect = ValueError("Cannot divide by zero")
        with patch('builtins.print') as mocked_print:
            self.controller.run()
            mocked_print.assert_called_with("Error: Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
