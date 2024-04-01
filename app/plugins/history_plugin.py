from app.commands import Command
from app.calculation_history_manager import CalculationHistoryManager
from mylogging import LoggingUtility

# Get a logger for this module
logger = LoggingUtility.get_logger('HistoryPlugin')

class History(Command):
    def __init__(self):
        self.manager = CalculationHistoryManager()

    def execute(self, *args):
        try:
            if not args or args[0] == 'view':
                df = self.manager.view_history()
                if df is not None:
                    print(df)
                else:
                    print("No history records found.")
            elif args[0] == 'clear':
                self.manager.clear_history()
                print("History cleared.")
            else:
                print("Invalid history command.")
            logger.info(f"Executed history command with args: {args}")
        except Exception as e:
            logger.error(f"Error executing history command: {e}")
            print("Failed to execute history command.")

