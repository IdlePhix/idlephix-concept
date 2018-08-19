"""
Contains helper methods for different consoles and shells in different platforms.
"""


__author__ = "Phixyn"


import os
import subprocess


def clear_screen():
    """
    Clear console and buffer
    """
    if os.name == "nt":
        os.system("cls")
    else:
        subprocess.call(["printf", "'\033c'"]) # https://stackoverflow.com/a/23075152
