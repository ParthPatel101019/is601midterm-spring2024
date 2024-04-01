
import os
import sys
import pkgutil
import importlib
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
import logging
from mylogging import LoggingUtility

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()

    def configure_logging(self):
        # Assuming you have a logging configuration in 'logging.conf' or similar
        LoggingUtility.configure_logging()
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        # Assuming plugins are located in 'app/plugins' and they are not packaged
        plugins_package = 'app.plugins'
        self.register_plugin_commands(plugins_package)

    def register_plugin_commands(self, package):
        module = importlib.import_module(package)
        for loader, module_name, is_pkg in pkgutil.iter_modules(module.__path__, module.__name__ + '.'):
            if not is_pkg:
                self.register_command(module_name)

    def register_command(self, module_name):
        try:
            module = importlib.import_module(module_name)
            for attr in dir(module):
                attr_obj = getattr(module, attr)
                if isinstance(attr_obj, type) and issubclass(attr_obj, Command) and attr_obj is not Command:
                    self.command_handler.register_command(attr.lower(), attr_obj())
                    logging.info(f"Command '{attr.lower()}' registered.")
        except ImportError as e:
            logging.error(f"Error loading command from '{module_name}': {e}")

    def start(self):
        self.load_plugins()
        logging.info("Calculator App started. Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip().lower()
            if command_input == 'exit':
                logging.info("Exiting Calculator App.")
                break
            try:
                parts = command_input.split()
                command_name = parts[0].lower()
                args = parts[1:]
                self.command_handler.execute_command(command_name, *args)
            except KeyError:
                logging.error(f"Unknown command: {command_input}")
        logging.info("Calculator App shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()

