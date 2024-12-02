"""
from akiraai.utils.logger_new import get_logger
import logging

logger = get_logger(
    name="test_logger",
    level=10,
    handler=logging.FileHandler("/workspaces/AkiraAI/logs/dummy.log")
)

logger.info("This is an Information Message")
logger.debug("This is a Debug Message")
logger.error("This is an Error Message")
logger.critical("This is a Critical Message")
logger.fatal("This is a Fatal Message")
"""


import logging
import os
from typing import Optional

# Default configurations
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure the log directory exists
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_FORMAT = (
    "%(asctime)s [%(levelname)s] [%(name)s] "
    "[%(filename)s:%(lineno)d] - %(message)s"
)
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Centralized formatter for all loggers
DEFAULT_FORMATTER = logging.Formatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT)

def get_logger(
    name: str,
    level: int = DEFAULT_LOG_LEVEL,
    handler: Optional[logging.Handler] = None,
    formatter: Optional[logging.Formatter] = None,
) -> logging.Logger:
    """
    Get a logger with the specified name. The logger will be configured with default settings unless otherwise specified.
    
    Args:
        name (str): The name of the logger.
        level (int): The logging level. Default is INFO.
        handler (Optional[logging.Handler]): A custom logging handler to add to the logger. If it's a FileHandler, ensure the filename is set or defaults to the logger name.
        formatter (Optional[logging.Formatter]): A custom formatter to set for the handlers. Default is None, which uses the global DEFAULT_FORMATTER.

    Returns:
        logging.Logger: The configured logger.
    """
    # Get the logger by name (or create one if it doesn't exist)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if the logger has already been configured
    if logger.hasHandlers():
        logger.handlers.clear()

    # Set formatter for the handler
    if handler:
        handler.setFormatter(formatter or DEFAULT_FORMATTER)
        logger.addHandler(handler)
    else:
        # If no handler is provided, use a default StreamHandler
        default_handler = logging.StreamHandler()
        default_handler.setFormatter(formatter or DEFAULT_FORMATTER)
        logger.addHandler(default_handler)

    return logger
