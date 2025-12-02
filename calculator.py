class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Current feature: Subtraction")
    print("Example: 10 - 3 =", calc.subtract(10, 3))