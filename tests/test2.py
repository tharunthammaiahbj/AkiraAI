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
named_logger = get_logger("custom_logger")

# Configure the named logger
named_logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()  # Add a handler explicitly
handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
named_logger.addHandler(handler)

# Log messages
named_logger.debug("This will not be shown (level is INFO).")
named_logger.info("Info message from the named logger.")
named_logger.warning("Warning message from the named logger.")





