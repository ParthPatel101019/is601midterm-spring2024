from app.commands import Command
import logging
from app.calculation_history_manager import CalculationHistoryManager


class Add(Command):
    def execute(self, operand1, operand2):
        result = float(operand1) + float(operand2)
        logging.info(f"Adding {operand1} and {operand2}: {result}")
        print(f"Result: {result}")
        
        history_manager = CalculationHistoryManager()
        history_manager.add_record('Add', operand1, operand2, result)

        return result
