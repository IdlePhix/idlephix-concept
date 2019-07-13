"""
Module containing the Game class for the game.
"""


__author__ = "Phixyn"



from chat import Chat
from player import Player
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
        # Player object
        self.player = Player("Phixyn")
        # Skills and items
        self._woodcutting = Woodcutting()
        self.player.add_skill(self._woodcutting)
        self._wood = Wood()
        self.player.add_item_to_inventory(self._wood)
        # Debug only
        # print(self.player.inventory)
        # print(self.player.skills)
        # exit()

        # Chat "window" area
        self._chat = Chat(max_messages=10)
        self._chat.add_message("Welcome to {textColorMagenta}IdlePhix{textFormatReset}.".
            format(textColorMagenta=terminal.TEXT_COLOR_MAGENTA, textFormatReset=terminal.TEXT_FORMATTING_RESET))

    def _increment_resources_and_exp(self):
        """
        Increments the amount of each item and gives experience points to the associated item's skill.
        """
        self._wood.chop()
        self._chat.add_message(self._wood.gatherMessage)

        # FIXME: For now, add_exp returns true if there was a level up
        if self._woodcutting.add_exp(self._wood.woodcuttingExpMultiplier):
            self._chat.add_message(self._woodcutting.get_level_up_message())

    def update(self):
        """
        Updates the game.
        """
        self._increment_resources_and_exp()

    def draw(self):
        """
        "Draws" the game "window".
        """
        terminal.clear_screen()
        print("Wood: {0} | Woodcutting exp: {1} | Woodcutting level: {2}".format(self._wood.amount, self._woodcutting.totalExperience, self._woodcutting.level))
        # print("Woodcutting exp (level): {0}".format(self.woodcutting.levelExperience)) # For debugging only
        self._chat.print()
