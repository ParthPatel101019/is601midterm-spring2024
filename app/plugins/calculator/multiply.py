from app.commands import Command

class MultiplyCommand(Command):
    def execute(self):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(f"{a} * {b} = {a * b}")
