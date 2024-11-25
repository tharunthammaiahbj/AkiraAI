from akiraai.utils.logging import get_logger
import logging

logger = get_logger("web-doc-loader")

logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    fmt=
    (
        "%(asctime)s [%(levelname)s] [%(name)s] "
        "[%(filename)s:%(lineno)d] - %(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


logger.error("this is an error message")
logger.info("This is an information : adjsjf")
logger.debug("This is a debug message and about it's things")
logger.warning("This is a warning message blah blah blah")
logger.fatal("this is a fatal message : blah blah blah")
logger.critical("critical message : blah blah")
