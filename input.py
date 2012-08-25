# Base classes for interpreting user input.
import sys


class InputReader(object):
    """
    Input reading base class. Controls prompt, which may display game data, and
    input reading and validation.
    """
    def __init__(self, game):
        self.game = game

    def read(self):
        """
        Prompt and read from stdin, returning a list of tokens.

        Prints the current value of self.prompt without a newline, then waits
        for command-line input. Returns the input, after passing it through the
        process command.
        """
        return self.process(raw_input(self.build_prompt()))

    def build_prompt(self):
        """Return a simple angle-bracket prompt."""
        return "> "


    def process(self, input):
        """
        Simply return the input as-is. Subclasses may override to provide more
        elaborate splitting, validation, etc.
        """
        return input

class CombatReader(InputReader):
    """
    Handles user input during combat. Displays party status before each prompt.
    """
    def build_prompt(self):
        return "combat >"
