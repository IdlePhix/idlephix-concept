"""
Module containing the Player class for the game.
"""


__author__ = "Phixyn"


class Player:
    """
    The Player class.
    """
    def __init__(self, name):
        """
        Class constructor method.
        """
        self.name = name
        self.inventory = {} # Items
        self.skills = {}    # Skils
        # self.currentAction = None
        self.currentAction = "Woodcutting"

    def add_item_to_inventory(self, item):
        """
        TODO
        """
        self.inventory[item["name"]] = item
    
    def add_skill(self, skill):
        """
        TODO
        """
        self.skills[skill["name"]] = skill

    def update_inventory_item(self, item):
        """
        TODO
        """
        # See if item in dict

    def update_skill(self, skill):
        """
        TODO
        """
        # See if skill in dict
        pass

    def set_action(self, action):
        """
        TODO
        """
        pass

    def update(self):
        """
        TODO
        """
        # Update based on current action
        # pass
        # if self.currentAction == "Woodcutting":
        self.update_skill(self.currentAction)
