from app.commands import Command
import logging
from app.calculation_history_manager import CalculationHistoryManager

class Divide(Command):
    def execute(self, operand1, operand2):
        # Adding a check to prevent division by zero
        if float(operand2) == 0:
            logging.warning("Attempted to divide by zero")
            print("Error: Division by zero is not allowed.")
            return
        result = float(operand1) / float(operand2)
        logging.info(f"Dividing {operand1} by {operand2}: {result}")
        print(f"Result: {result}")
        history_manager = CalculationHistoryManager()
        history_manager.add_record('Divide', operand1, operand2, result)
        return result
