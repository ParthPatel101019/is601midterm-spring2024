from app.command import Command
import logging

class Subtract(Command):
    def execute(self, operand1, operand2):
        result = float(operand1) - float(operand2)
        logging.info(f"Subtracting {operand2} from {operand1}: {result}")
        print(f"Result: {result}")
