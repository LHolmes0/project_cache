import logging.handlers

APP_NAME = "Project-Cache"
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# since unicorn logger add asctime we do not need it here as well as app name
formatter = logging.Formatter("%(levelname)s: %(message)s")

# stop file logging for now
# file_logging = logging.handlers.RotatingFileHandler(f"{APP_NAME}.log", maxBytes=10_485_760, backupCount=10)
# file_logging.setFormatter(formatter)
# logger.addHandler(file_logging)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
