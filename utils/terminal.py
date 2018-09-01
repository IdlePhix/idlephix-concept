"""
Contains helper methods for different terminals and shells in different
platforms.
"""


__author__ = "Phixyn"


import os


# ANSI escape sequences - Select Graphic Rendition subset. Allows formatting
# text in text terminals. All of these have the form "\033[XXXm" where XXX
# is a series of semicolon-separated parameters.
# More information: https://en.wikipedia.org/wiki/ANSI_escape_code
TEXT_COLOR_MAGENTA = "\033[38;35m"
TEXT_COLOR_MAGENTA_BOLD = "\033[38;35;1m"
TEXT_FORMATTING_RESET = "\033[0m" # Resets the text formatting back to default


def clear_screen():
    """
    Clear console and buffer
    """
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033c", end="") # https://stackoverflow.com/a/23075152
