from .logger_config import setup_logger
from . import *
logger = setup_logger(__name__)

def main():
    logger.info("App started")
    #agent = Agent()
    mindmap = Mindmap(None)
    mindmap.traversequestion()
if __name__ == "__main__":
    main()
