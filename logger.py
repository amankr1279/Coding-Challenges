import logging

def setup_logger(name):
    """Set up a logger with the specified name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Avoid adding multiple handlers to the logger
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        
        file_handler = logging.FileHandler(name + ".log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        logger.addHandler(file_handler)
    
    return logger