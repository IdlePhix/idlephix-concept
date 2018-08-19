#!/usr/bin/env python3
"""Concept work for IdlePhix.

Increments things (?).
"""


__author__ = "Phixyn"
__version__ = "v0.0.1"


import sys
import time
from game import Game
from util import terminal
from util.logger import logger


if __name__ == "__main__":
    game = Game()

    try:
        while True:
            terminal.clear_screen()
            game.update()
            game.draw()
            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        print()
        logger.info("Exiting.")
        sys.exit(0)
