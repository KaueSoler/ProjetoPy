from calculator.model import CalculatorModel

class CalculatorService:
    def __init__(self):
        self.model = CalculatorModel()

    def perform_operation(self, operation, *args):
        if operation == 'add':
            return self.model.add(*args)
        elif operation == 'subtract':
            return self.model.subtract(*args)
        elif operation == 'multiply':
            return self.model.multiply(*args)
        elif operation == 'divide':
            return self.model.divide(*args)
        elif operation == 'power':
            return self.model.power(*args)
        elif operation == 'sqrt':
            return self.model.sqrt(*args)
        else:
            raise ValueError("Unknown operation")
