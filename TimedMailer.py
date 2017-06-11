from utils import logger
import logging
import ConfigParser

CONFIG_FILE_NAME = "cfg.ini"

config = ConfigParser.ConfigParser()
logger = logger.create_logger()

if __name__ == '__main__':
    config.read(CONFIG_FILE_NAME)
    logger.info("Hello!")
    
