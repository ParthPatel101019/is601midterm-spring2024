from app.command import Command
import logging

class Add(Command):
    def execute(self, operand1, operand2):
        result = float(operand1) + float(operand2)
        logging.info(f"Adding {operand1} and {operand2}: {result}")
        print(f"Result: {result}")
