from calculator.service import CalculatorService
from calculator.view import CalculatorView

class CalculatorController:
    def __init__(self):
        self.service = CalculatorService()
        self.view = CalculatorView()

    def run(self):
        while True:
            try:
                operation, *args = self.view.get_user_input()
                result = self.service.perform_operation(operation, *args)
                self.view.display_result(result)
            except ValueError as e:
                self.view.display_error(str(e))
