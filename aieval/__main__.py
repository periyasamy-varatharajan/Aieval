from .logger_config import setup_logger
from . import *
logger = setup_logger(__name__)

def main():
    logger.info("App started")
    agent = Agent()
    mindchat = Chat(agent)
    mindmap = Mindmap(mindchat)
    mindmap.traversequestion()
if __name__ == "__main__":
    main()
