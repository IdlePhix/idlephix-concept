#!/usr/bin/env python3
"""Concept work for IdlePhix.

Increments things (?).
"""


__author__ = "Phixyn"
__version__ = "v0.0.1"


from chat import Chat
import sys
import time
from util import console
from util.logger import logger


class Game:
    """
    The Game class.
    """
    # TODO: make certain methods and variables private
    def __init__(self):
        """
        Default constructor.
        """
        # Chat "window" area
        self._chat = Chat(max_messages=7)
        self._chat.add_message("Welcome to IdlePhix.")

        # Item and skills
        self.wood = 0
        self.woodMultiplier = 1 # TODO depends on axe/hatchet item (part of item configuration)

        self.woodcuttingLevel = 1
        self.woodcuttingExp = 0
        self.woodcuttingExpMultiplier = 0.5 # TODO should be per item (part of item configuration)

    def _increment_resources(self):
        """
        Increments the quantity of each item.
        """
        self._chat.add_message("You chop down some wood.")
        self.wood += self.woodMultiplier

    def _increment_exp(self):
        """
        Increments experience points of each skill.
        """
        self.woodcuttingExp += self.woodcuttingExpMultiplier

    def update(self):
        """
        Updates the game.
        """
        self._increment_resources()
        self._increment_exp()

    def draw(self):
        """
        "Draws" the game "window".
        """
        print("Wood: {0} | Woodcutting exp: {1} | Woodcutting level: {2}".format(self.wood, self.woodcuttingExp, self.woodcuttingLevel))
        self._chat.print_chat()


if __name__ == "__main__":
    game = Game()

    try:
        while True:
            console.clear_screen()
            game.update()
            game.draw()
            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        print()
        logger.info("Exiting.")
        sys.exit(0)
