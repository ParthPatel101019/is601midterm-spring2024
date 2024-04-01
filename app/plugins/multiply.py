from app.commands import Command
import logging
from app.calculation_history_manager import CalculationHistoryManager

class Multiply(Command):
    def execute(self, operand1, operand2):
        result = float(operand1) * float(operand2)
        logging.info(f"Multiplying {operand1} and {operand2}: {result}")
        print(f"Result: {result}")
        history_manager = CalculationHistoryManager()
        history_manager.add_record('Multiply', operand1, operand2, result)
        return result
