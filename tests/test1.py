from akiraai.utils.logging import (
    get_logger,
    set_verbosity_info,
    set_verbosity,
    set_verbosity_error,
    set_verbosity_debug,
    set_verbosity_fatal,
    set_verbosity_warning,
    get_verbosity,
    setDEFAULT_HANDLER,
    set_handler
)
import logging

# Get a named logger
logger = get_logger("custom_logger")

# Configure the named logger
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()  # Add a handler explicitly
handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
logger.addHandler(handler)

# Log messages
logger.debug("This will not be shown (level is INFO).")
logger.info("Info message from the named logger.")
logger.warning("Warning message from the named logger.")

logger.error("1: ERROR:this is an error message")
logger.info("1: INFO: This is an information")
logger.debug("1: DEBUG: this is a debug message")


logger.error("2: ERROR:this is an error message")
logger.info("2: INFO: This is an information")
logger.debug("2: DEBUG: this is a debug message")


logger.error("3: ERROR:this is an error message")
logger.info("3: INFO: This is an information")
logger.debug("3: DEBUG: this is a debug message")





