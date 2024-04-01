from app.commands import Command
import sys

class ExitCommand(Command):
    def execute(self):
        print("Exiting the calculator.")
        sys.exit(0)

