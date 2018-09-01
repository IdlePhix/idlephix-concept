"""
Module containing the Wood item class for the game.
"""


__author__ = "Phixyn"


from utils import terminal


class Wood:
    """
    Class for all types of wood log items.

    Right now, it is used for the only Wood log item, but it should be subclassed in the future.
    """
    def __init__(self):
        """
        Class constructor method.
        """
        self.name = "Wood"
        # TODO woodcutting level required
        self.amount = 0
        self._gatherMultiplier = 1 # TODO depends on axe/hatchet item (part of item configuration)
        self.gatherMessage = "You chop down some {textColorMagentaBold}wood{textFormatReset}.".\
            format(textColorMagentaBold=terminal.TEXT_COLOR_MAGENTA_BOLD, textFormatReset=terminal.TEXT_FORMATTING_RESET)
        self.woodcuttingExpMultiplier = 0.5 # Should be part of the item configuration (rename to skillExpMultiplier?)
        # TODO: lol sleepless night gg
        # self.experienceRewards = {"Woodcutting": 0.5, "RandomSkill": 1}
        self.experienceRewards = {"Woodcutting": 0.5}

    def chop(self):
        """
        Adds wood to the inventory.
        """
        self.amount += self._gatherMultiplier
