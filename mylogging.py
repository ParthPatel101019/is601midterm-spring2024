import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LoggingUtility:
    @staticmethod
    def configure_logging():
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        log_file = os.getenv('LOG_FILE', 'app.log')

        logging.basicConfig(
            filename=log_file,
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)

