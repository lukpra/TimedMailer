import logging

def create_logger(logger_name=__name__, logger_file=None, logger_level=logging.DEBUG):

    # Create default logger
    logger = logging.getLogger(logger_name)
    
    # If log level is set to None, dont log
    if logger_level is None:
        logger.hnadlers = [logging.NullHandler()]
        LOGGER = logger
        return logger

    logger.setLevel(logger_level)

    # Stream to terminal handler
    handlers = [logging.StreamHandler()]  

    # Stream to file handler
    if logger_file:
         handlers.append(logging.FileHandler(logger_file))

    # Create log formatter
    log_formatter =  logging.Formatter("%(asctime)s [%(levelname)s] : %(message)s", "%Y-%m-%d %H:%M:%S")

    # Add formatter to handlers
    for handler in handlers :
        handler.setFormatter(log_formatter)

    # Add handlers to login
    logger.handlers = handlers

    return logger
    
if __name__ == '__main__':
    log = create_logger(logger_name="test_logger")
    log.debug("Hello World!")


