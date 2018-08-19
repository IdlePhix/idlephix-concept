#!/usr/bin/env python3
"""Concept work for IdlePhix.

Increments things (?).
"""


__author__ = "Phixyn"
__version__ = "v0.0.1"


import sys
import time
from util import console
from util.logger import logger


class Game:
    """
    The Game class.
    """
    def __init__(self):
        """
        Default constructor.
        """
        # Item and skills
        self.wood = 0
        self.woodMultiplier = 1 # TODO depends on axe/hatchet item (part of item configuration)

        self.woodcuttingLevel = 1
        self.woodcuttingExp = 0
        self.woodcuttingExpMultiplier = 0.5 # TODO should be per item (part of item configuration)

    def increment_resources(self):
        """
        Increments the quantity of each item.
        """
        self.wood += self.woodMultiplier

    def increment_exp(self):
        """
        Increments experience points of each skill.
        """
        self.woodcuttingExp += self.woodcuttingExpMultiplier

    def update(self):
        """
        Updates the game.
        """
        self.increment_resources()
        self.increment_exp()


if __name__ == "__main__":
    game = Game()

    try:
        while True:
            console.clear_screen()
            game.update()

            # "Draw()"
            print("\nWelcome to IdlePhix.\n")
            logger.info("Wood: {0}".format(game.wood))
            logger.info("Woodcutting exp: {0}".format(game.woodcuttingExp))
            logger.info("Woodcutting level: {0}".format(game.woodcuttingLevel))

            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        logger.info("Exiting.")
        sys.exit(0)
