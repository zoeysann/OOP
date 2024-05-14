class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"


calc = Calculator()

print("Addition:", calc.add(5, 3)) 
print("Subtraction:", calc.subtract(7, 2))
print("Multiplication:", calc.multiply(4, 6))
print("Division:", calc.divide(10, 2))
print("Division:", calc.divide(10, 0))

