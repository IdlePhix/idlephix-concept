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


# Item and skills
wood = 0
woodMultiplier = 1 # TODO depends on axe/hatchet item (part of item configuration)

woodcuttingLevel = 1
woodcuttingExp = 0
woodcuttingExpMultiplier = 0.5 # TODO should be per item (part of item configuration)


# def increment_resources():
#     """
#     Increments the quantity of each item.
#     """
#     wood += woodMultiplier
# 
# 
# def increment_exp():
#     """
#     Increments experience points of each skill.
#     """
#     woodcuttingExp += woodcuttingExpMultiplier


if __name__ == "__main__":
    try:
        while True:
            console.clear_screen()
            
            # "Update()"
            # increment_resources()
            # increment_exp()

            # "Draw()"
            print("\nWelcome to IdlePhix.\n")
            logger.info("Wood: {0}".format(wood))
            logger.info("Woodcutting exp: {0}".format(woodcuttingExp))
            logger.info("Woodcutting level: {0}".format(woodcuttingLevel))
            wood += woodMultiplier
            woodcuttingExp += woodcuttingExpMultiplier

            time.sleep(1) # tfw not using delta
    except KeyboardInterrupt as ex:
        logger.info("Exiting.")
        sys.exit(0)
