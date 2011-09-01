# Classes which map user input to commands.
import re


class Interpreter:
    """Base class for interpreting user input."""
    def __init__(self, game):
        self.game = game

    def tokenize(self, s):
        """Naive string tokenization implementation: return a list of words, or
        None if no string or an empty string was provided. Simply splits on
        whitespace under the hood."""
        return s.split() if s else None

    def interpret(self, user_input):
        """Template method for command interpretation. Subclasses must implement."""
        words = self.tokenize(user_input)
        
        if words is not None and not re.match(r"\s+", words[0]):
            command = self.find_command(words[0])
            if command:
                command(words[1:] or None)
            else:
                self.game.writer.writecr(
                    "I don't know what '%s' means." % user_input)
        else:
            pass
            # TODO: raise an exception or something

    def find_command(self, action_name):
        """Search self.commands for a matching pattern and return the
        corresponding command function."""
        for pattern, command in self.commands:
            if re.match(pattern, action_name):
                return command
        return None


class ExplorationInterpreter(Interpreter):
    """All commands in exploration mode."""
    def __init__(self, game):
        Interpreter.__init__(self, game)
        self.commands = (
            (r"l(ook)?",            self.look),
            (r"i(nv(entory)?)?",    self.inventory),
            # yes, the long names are actually aliases for the short ones
            (r"e(ast)?",            self.move_command("e")),
            (r"w(est)?",            self.move_command("w")),
            (r"n(orth)?",           self.move_command("n")),
            (r"s(outh)?",           self.move_command("s")),
            (r"up?",                self.move_command("u")),
            (r"d(own)?",            self.move_command("d")),
            (r"(z|wait)",           self.wait),
        )

    def look(self, arguments=None):
        self.game.writer.write_room(self.game.area.location, "verbose")

    def inventory(self, arguments=None):
        self.game.writer.writecr("Inventory is not yet implemented.")

    def wait(self, arguments=None):
        self.game.writer.writecr("Time passes.")

    def move_command(self, direction):
        """Returns a function which attempts to move in the stated direction."""

        def command(arguments=None):
            if self.game.area.move(direction) is not None:
                self.game.writer.write_room(self.game.area.location)
            else:
                self.game.writer.writecr("There is no exit in this direction.")

        return command
