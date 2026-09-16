import logging
# logging.basicConfig(level=logging.DEBUG)

def get_logger(name):
    logger = logging.getLogger(name) #creating the logger obj
    logger.setLevel(logging.DEBUG) # allows DEBUG and higher level msgs
    
    if not logger.handlers:
        handler = logging.StreamHandler() # sends logs to the terminal
        handler.setLevel(logging.DEBUG) # allows the handler to output DEBUG and above
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") # controls the appearance of the log

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger