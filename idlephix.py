#!/usr/bin/env python3
"""Concept work for IdlePhix.

Increments things (?).
"""


__author__ = "Phixyn"
__version__ = "v1.0.0"


import sys
import time
from game import Game
from utils.logger import logger


if __name__ == "__main__":
    game = Game()

    try:
        while True:
            # Event handling, if needed/applicable, goes here
            game.update()
            # terminal.clear_screen() # moved to game.draw()
            game.draw()
            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        print()
        logger.info("Exiting.")
        sys.exit(0)
