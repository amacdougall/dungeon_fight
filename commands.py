"""
Core module containing all commands which can be invoked by user input. Pass
these classes as parameters to Interpreter class constructors.
"""


class ExplorationCommands(object):
    """
    All commands used in exploration mode.
    """
    def __init__(self, game):
        self.game = game
        # Note that the first matching pattern will be used
        self.patterns = (
            (r"(quit|exit)$",       self.exit),
            (r"l(ook)?$",           self.look),
            (r"i(nv(entory)?)?$",   self.inventory),
            # yes, the long names are actually aliases for the short ones
            (r"e(ast)?$",           self.move_command("e")),
            (r"w(est)?$",           self.move_command("w")),
            (r"n(orth)?$",          self.move_command("n")),
            (r"s(outh)?$",          self.move_command("s")),
            (r"up?$",               self.move_command("u")),
            (r"d(own)?$",           self.move_command("d")),
            (r"(z|wait)$",          self.wait),
        )

    # TODO: better implementation of everything?
    def look(self):
        self.game.writer.write_room(self.game.area.location, "verbose")

    def inventory(self):
        self.game.writer.writecr("Inventory is not yet implemented.")

    def wait(self):
        self.game.writer.writecr("Time passes.")

    def move_command(self, direction):
        def command():
            if self.game.area.move(direction) is not None:
                self.game.writer.write_room(self.game.area.location)
            else:
                self.game.writer.writecr("There is no exit in this direction.")

        return command

    def exit(self):
        self.game.exit_requested = True
