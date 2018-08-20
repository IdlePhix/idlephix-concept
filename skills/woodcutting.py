"""
Module containing the Woodcutting skill class for the game.
"""


__author__ = "Phixyn"


# from util import terminal


class Woodcutting:
    """
    Class for the Woodcutting skill.
    """
    def __init__(self):
        """
        Class constructor method.
        """
        self.level = 1
        self.totalExperience = 0
        self.levelExperience = 0
        self._expPerLevel = 25 # Experience needed to level up
        self.levelUpMessage = "Congratulations, you have leveled up {textColorMagentaBold}woodcutting{textFormatReset}. You are now level {woodcuttingLevel}."

    def add_exp(self, exp):
        """
        Adds experience points to the skill and increments level if needed.

        For now, this method returns True if the skill has leveled up. This is so
        that the Game class can add a message to the chat "window" to inform the
        player that they leveled up.
        """
        self.totalExperience += exp
        self.levelExperience += exp
        # Handle levelling up
        if self.levelExperience >= self._expPerLevel:
            self.level += 1
            # (Re)set level experience points, adding any leftover from the level up
            self.levelExperience = self.levelExperience % self._expPerLevel
            return True
        else:
            return False