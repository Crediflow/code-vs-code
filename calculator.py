class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Current features: Addition and Subtraction")
    print("Example: 5 + 3 =", calc.add(5, 3))
    print("Example: 10 - 4 =", calc.subtract(10, 4))