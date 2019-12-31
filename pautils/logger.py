import logging
import logging.handlers as handlers
import os
import sys
from pythonjsonlogger import jsonlogger

# json_logging.ENABLE_JSON_LOGGING = True
# json_logging.init_non_web()

levels = { 
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'NOTSET': logging.NOTSET, 
}
loglevel = levels[os.environ.get('LOG_LEVEL', 'DEBUG')]
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)

logHandler = logging.StreamHandler()
format_str = '%(filename)%(lineno)%(message)%(levelname)%(name)%(asctime)'
formatter = jsonlogger.JsonFormatter(format_str)
logHandler.setFormatter(formatter)
logger.setLevel(loglevel)
logger.addHandler(logHandler)
