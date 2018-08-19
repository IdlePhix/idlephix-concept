"""
Module containing the Game class for the game.
"""


__author__ = "Phixyn"


from chat import Chat
from util import terminal
# from util.logger import logger


class Game:
    """
    The Game class.
    """
    def __init__(self):
        """
        Default constructor.
        """
        # Chat "window" area
        self._chat = Chat(max_messages=7)
        self._chat.add_message("Welcome to {textColorMagenta}IdlePhix{textFormatReset}.".
            format(textColorMagenta=terminal.TEXT_COLOR_MAGENTA, textFormatReset=terminal.TEXT_FORMATTING_RESET))

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
        self._chat.add_message("You chop down some {textColorMagentaBold}wood{textFormatReset}.".
            format(textColorMagentaBold=terminal.TEXT_COLOR_MAGENTA_BOLD, textFormatReset=terminal.TEXT_FORMATTING_RESET))
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