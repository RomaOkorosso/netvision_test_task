import logging
from datetime import datetime

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create file handler
filename = f"./logs/{datetime.now().date()}.log"
fh = logging.FileHandler(filename)
fh.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)


def log(msg: str):
    logger.info(msg)
