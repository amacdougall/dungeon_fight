# Base classes for interpreting user input.
import sys


class InputReader:
    """Input reading base class."""
    def __init__(self):
        self.prompt = "> "

    def read(self):
        """Prompt and read from stdin, returning a list of tokens.

        Prints the current value of self.prompt without a newline, then waits
        for command-line input. Returns a list of the input words, split using
        the default str.split().
        """
        print self.prompt,  # trailing comma ensures no newline after prompt
        # input = sys.stdin.readline()
        return self.process(sys.stdin.readline())

    def process(self, input):
        """Process the input by simply splitting it on whitespace."""
        return input.split()
