"""
Module containing the Chat class for the game.
"""


__author__ = "Phixyn"


class Chat:
    """
    The Chat "window" class.
    """
    def __init__(self, max_messages=5):
        """
        Class constructor method.
        """
        self._messages = []
        self._maxMessages = max_messages
    
    def add_message(self, message):
        """
        Adds a message to the chat. If the array of messages exceeds the maximum message
        limit, then the oldest chat message is removed from the array.
        """
        self._messages.append(message)
        if len(self._messages) > self._maxMessages:
            del(self._messages[0])

    def clear(self):
        """
        Removes all the chat messages from the messages array.
        """
        self._messages.clear()

    def print(self):
        """
        Prints all the chat messages in the messages array.
        """
        print("\n"*3) # TODO naughty magic number
        for message in self._messages:
            print(message)
