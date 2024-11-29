import logging
from typing import List
from akiraai.utils.logging import get_logger
from akiraai.nodes.base_node import BaseNode


logger = get_logger("node-logger")
logger.setLevel(logging.DEBUG)
handler =logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    fmt=
    (
        "%(asctime)s [%(levelname)s] [%(name)s] "
        "[%(filename)s:%(lineno)d] - %(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


