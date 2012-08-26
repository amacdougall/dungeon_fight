# Classes which map user input to commands.
import re
import pdb


class Interpreter(object):
    """
    Base class for reading and interpreting user input. Call next_command() to
    prompt for user input and convert it to a game logic method call.
    Interpreter classes should never have to do game logic, and game logic
    should never have to interpret strings.

    The commands argument may be any object which has a patterns property; a
    patterns object must be a tuple or list of (pattern, command) tuples or
    lists. This pattern mapping will be used to match command names with command
    functions.

    The command functions can come from anywhere, but will probably be
    references to methods on the commands object. The commands object is
    required to have the following commands: "command_not_found" and
    "command_is_whitespace".
    """
    def __init__(self, commands):
        self.commands = commands

    def read(self):
        """
        Prompt and read from stdin, returning output usable by interpret().
        Calls build_prompt() to prompt for input, and process() to generate
        interpretable output.
        """
        return self.process(raw_input(self.build_prompt()))

    def build_prompt(self):
        """
        Return a simple angle-bracket prompt. Subclasses may override to provide
        status information or other data or decoration along with the prompt.
        """
        return "> "

    def process(self, user_input):
        """
        Convert the raw user input string into a form usable by interpret().
        This implementation uses the default tokenize(), but subclasses may
        override this, tokenize(), or both.
        """
        return self.tokenize(user_input)

    def tokenize(self, string=""):
        """
        Naive string tokenization implementation: return a list of words, or
        None if no string or an empty string was provided. Simply splits on
        whitespace under the hood, after stripping leading and trailing
        whitespace.
        """
        return string.strip().split()

    def next_command(self):
        """
        Interpret the user input, ultimately calling a game logic command.
        Subclasses probably do not have to override this method as long as they
        implement read() and interpret().
        """
        self.interpret(self.read())

    def interpret(self, tokens=None):
        """
        Given a list of tokens, find an appropriate command in the commands
        object and invoke it with appropriate arguments. Subclasses must
        implement; this example implementation simply finds the base command by
        matching the first argument, and executes it without further arguments.
        """
        if tokens is None:
            raise "Interpret.interpret(): no tokens provided."

        command = self.find_command(tokens[0])

        if command:
            command()
        else:
            commands.command_not_found()

    def find_command(self, name):
        """
        Search self.commands.patterns for the first matching pattern and return
        the corresponding command function.
        """
        for pattern, command in self.commands.patterns:
            if re.match(pattern, name):
                return command
        return None

class ExplorationInterpreter(Interpreter):
    pass
