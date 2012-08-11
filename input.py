# Base classes for interpreting user input.
import sys


class InputReader(object):
    """Input reading base class."""
    def __init__(self):
        self.prompt = "> "

    def read(self):
        """Prompt and read from stdin, returning a list of tokens.

        Prints the current value of self.prompt without a newline, then waits
        for command-line input. Returns a list of the input words, split using
        the default str.split()."""
        return self.process(raw_input(self.prompt))

    def process(self, input):
        """Process the input by simply splitting it on whitespace."""
        return input.split()


class ExplorationReader(InputReader):
    """Input reader for exploration."""
    def __init__(self):
        self.prompt = "> "

    def read(self):
        """Prompt and read from stdin, returning a single word."""
        return self.process(raw_input(self.prompt))

    def process(self, input):
        """Process the input by validating it against allowed inputs."""
        return input
