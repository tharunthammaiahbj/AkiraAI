from akiraai.utils.logging import get_logger
import logging

logger = get_logger(
    name="test_logger",
    level=10
)

logger.info("This is an Information Message")
logger.debug("This is a Debug Message")
logger.error("This is an Error Message")
logger.critical("This is a Critical Message")
logger.fatal("This is a Fatal Message")
