#!/usr/bin/env python3
"""Concept work for IdlePhix.

Increments things (?).
"""


__author__ = "Phixyn"
__version__ = "v0.0.2"


import sys
import time
from game import Game
from utils import terminal
from utils.logger import logger


if __name__ == "__main__":
    game = Game()

    try:
        while True:
            terminal.clear()
            game.update()
            game.draw()
            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        print()
        logger.info("Exiting.")
        sys.exit(0)
