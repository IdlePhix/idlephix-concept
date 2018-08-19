"""
Logger utility for the game.

Logs messages to STDOUT and to a file if desired. The logger object is set up
with handlers using formatters that use a clean and concise format for logging
messages.
"""


__author__ = "Phixyn"


import logging
import os
import sys
import time


# Logging setup
LOGS_FOLDER_NAME = "logs"
# Save log files with the project, date and time in the name
# (e.g. ProjectName_2017-10-11_09-55.log)
LOG_FILE_NAME = time.strftime("IdlePhix_%Y-%m-%d_%H-%M.log")
LOG_FILE_PATH = "{0}/{1}/{2}".format(os.getcwd(), LOGS_FOLDER_NAME, LOG_FILE_NAME)
LOG_LEVEL = logging.DEBUG

# Create a Formatter to specify how logging messages are displayed
# e.g. [2017-08-28 01:04:55][INFO] Some information
LOG_FORMATTER = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Create logs folder if it is not present:
# if not os.path.isdir(LOGS_FOLDER_NAME):
#     os.mkdir(LOGS_FOLDER_NAME)

# Set up logging
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

# Create and add logging handler for file logging
# Note: logging to files is disabled
# loggerFileHandler = logging.FileHandler(LOG_FILE_PATH)
# loggerFileHandler.setFormatter(LOG_FORMATTER)
# logger.addHandler(loggerFileHandler)

# Create and add logging handler for STDOUT (console) logging
loggerConsoleHandler = logging.StreamHandler(sys.stdout)
loggerConsoleHandler.setFormatter(LOG_FORMATTER)
logger.addHandler(loggerConsoleHandler)
