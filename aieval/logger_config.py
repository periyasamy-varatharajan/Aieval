import logging
from pathlib import Path

def setup_logger(name: str = __name__):
    log_file = Path("app.log")

    logging.basicConfig(
        level=logging.DEBUG,  # change to INFO for production
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler(log_file, mode="a", encoding="utf-8"),
            #logging.StreamHandler(),  # console
        ],
    )
    return logging.getLogger(name)
