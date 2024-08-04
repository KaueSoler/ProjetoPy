class CalculatorView:
    def display_result(self, result):
        print(f"Result: {result}")

    def display_error(self, error_message):
        print(f"Error: {error_message}")

    def get_user_input(self):
        operation = input("Enter operation (add, subtract, multiply, divide, power, sqrt): ")
        if operation == 'sqrt':
            value = float(input("Enter value: "))
            return operation, value
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return operation, a, b
