# Classes which map user input to commands.
import re


class Interpreter:
    """Base class for interpreting user input."""

    def tokenize(self, s):
        """Naive string tokenization implementation: return a list of words, or
        None if no string or an empty string was provided."""
        return s.split() if s else None

    def interpret(user_input):
        """Template method for command interpretation. Subclasses must implement."""
        words = self.tokenize(user_input)
        
        if words is not None:
            command = Command()
            command.action = words.shift()
            if len(words) > 0:
                command.arguments = list(words)  # copy
        else:
            return None  # TODO: raise an exception or something


class Command:
    def __init__(self):
        action = None
        arguments = None
