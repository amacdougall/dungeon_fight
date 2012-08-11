# Classes which map user input to commands.
import re


class Interpreter(object):
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

        # remember that the first matching pattern executes
        self.commands = (
            (r"(quit|exit)",        self.game.exit),
            (r"l(ook)?",            self.game.look),
            (r"i(nv(entory)?)?",    self.game.inventory),
            # yes, the long names are actually aliases for the short ones
            (r"e(ast)?",            self.game.move_command("e")),
            (r"w(est)?",            self.game.move_command("w")),
            (r"n(orth)?",           self.game.move_command("n")),
            (r"s(outh)?",           self.game.move_command("s")),
            (r"up?",                self.game.move_command("u")),
            (r"d(own)?",            self.game.move_command("d")),
            (r"(z|wait)",           self.game.wait),
        )
