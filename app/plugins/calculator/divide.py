from app.commands import Command

class DivideCommand(Command):
    def execute(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{a} / {b} = {a / b}")
