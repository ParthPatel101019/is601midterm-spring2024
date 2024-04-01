import pandas as pd
import os
from mylogging import LoggingUtility
import warnings


# Configure logging for this module
logger = LoggingUtility.get_logger('CalculationHistoryManager')

class CalculationHistoryManager:
    def __init__(self, filename='calculation_history.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result']).to_csv(self.filename, index=False)
        logger.info(f"History manager initialized with file: {self.filename}")

    def add_record(self, operation, operand1, operand2, result):
        try:
            df = pd.read_csv(self.filename)
            
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", FutureWarning)
                df = df._append({'Operation': operation, 'Operand1': operand1, 'Operand2': operand2, 'Result': result}, ignore_index=True)
            df.to_csv(self.filename, index=False)
            logger.info(f"Record added: {operation} {operand1} {operand2} = {result}")
        except Exception as e:
            logger.error(f"Failed to add record: {e}")

    def view_history(self):
        try:
            if os.path.exists(self.filename):
                df = pd.read_csv(self.filename)
                logger.info("History viewed.")
                return df
            else:
                logger.warning("Attempted to view history, but history file does not exist.")
        except Exception as e:
            logger.error(f"Failed to view history: {e}")

    def clear_history(self):
        try:
            pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result']).to_csv(self.filename, index=False)
            logger.info("History cleared.")
        except Exception as e:
            logger.error(f"Failed to clear history: {e}")

