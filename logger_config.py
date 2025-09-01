import logging

def setup_logger(name, log_file='currency.log', level=logging.DEBUG):
   
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # File handler (all levels)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        # Console handler (INFO and above)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger
