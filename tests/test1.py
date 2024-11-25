from akiraai.utils.logging import (
    get_logger,
    set_verbosity_info,
    set_verbosity,
    set_verbosity_error,
    set_verbosity_debug,
    set_verbosity_fatal,
    set_verbosity_warning,
    get_verbosity,
    setDEFAULT_HANDLER
)


logger1 =get_logger("testing-logger")
print(get_verbosity())


print(f"Current Verbosity LvL: {get_verbosity()}")

logger1.error("1: ERROR:this is an error message")
logger1.info("1: INFO: This is an information")
logger1.debug("1: DEBUG: this is a debug message")

set_verbosity(20)

print(f"Current Verbosity LvL: {get_verbosity()}")

logger1.error("2: ERROR:this is an error message")
logger1.info("2: INFO: This is an information")
logger1.debug("2: DEBUG: this is a debug message")

set_verbosity(10)

print(f"Current Verbosity LvL: {get_verbosity()}")

logger1.error("3: ERROR:this is an error message")
logger1.info("3: INFO: This is an information")
logger1.debug("3: DEBUG: this is a debug message")


    