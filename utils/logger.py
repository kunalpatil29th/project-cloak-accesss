"""
Project Cloak Access: utils - logger.py

Definition:
Logging: The process of recording events and messages that occur during the execution of a software 
application. It is essential for debugging and monitoring the system's state.

Concepts:
1. Log Levels: Categorization of logs based on their severity (DEBUG, INFO, WARNING, ERROR, CRITICAL).
2. Formatters: Components that define the layout and content of the log messages.
"""

import logging
import sys

def setup_logger(name="CloakProject"):
    """
    Sets up a basic logger for the project.
    
    Definition: Logger - An object that provides methods for logging messages.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create console handler
    # Definition: Handler - A component that sends log records to their destination (e.g., console, file).
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Initialize a default logger
logger = setup_logger()
