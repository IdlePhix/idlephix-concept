"""
Module containing the Game class for the game.
"""


__author__ = "Phixyn"


from chat import Chat
from items.wood import Wood
from skills.woodcutting import Woodcutting
from utils import terminal
# from util.logger import logger


class Game:
    """
    The Game class.
    """
    def __init__(self):
        """
        Class constructor method.
        """
        # Chat "window" area
        self._chat = Chat(max_messages=10)
        self._chat.add_message("Welcome to {textColorMagenta}IdlePhix{textFormatReset}.".
            format(textColorMagenta=terminal.TEXT_COLOR_MAGENTA, textFormatReset=terminal.TEXT_FORMATTING_RESET))

        # Skills and items
        self.woodcutting = Woodcutting()
        self.wood = Wood()

    def _increment_resources_and_exp(self):
        """
        Increments the amount of each item and gives experience points to the associated item's skill.
        """
        self.wood.chop()
        self._chat.add_message(self.wood.gatherMessage)

        # For now, add_exp returns true if there was a level up
        if self.woodcutting.add_exp(self.wood.woodcuttingExpMultiplier):
            # TODO using .format here is a bit bad e_e
            self._chat.add_message(self.woodcutting.levelUpMessage.
                format(textColorMagentaBold=terminal.TEXT_COLOR_MAGENTA_BOLD,
                    textFormatReset=terminal.TEXT_FORMATTING_RESET,
                    woodcuttingLevel=self.woodcutting.level))

    def update(self):
        """
        Updates the game.
        """
        self._increment_resources_and_exp()

    def draw(self):
        """
        "Draws" the game "window".
        """
        print("Wood: {0} | Woodcutting exp: {1} | Woodcutting level: {2}".format(self.wood.amount, self.woodcutting.totalExperience, self.woodcutting.level))
        # print("Woodcutting exp (level): {0}".format(self.woodcutting.levelExperience)) # For debugging only
        self._chat.print()
