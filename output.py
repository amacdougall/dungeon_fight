# Output classes which write to file-like objects.
import textwrap


class Writer:
    """Base class for writing output."""

    def __init__(self, *args):
        self.outputs = list(args)
        self.wrap_function = textwrap.wrap  # default text wrap function
        self.line_separator = "\n"
        self.debug = False

    def write(self, message):
        """Write the message to all available outputs."""
        if len(self.outputs) == 0:
            raise "Writer.write: no outputs available"

        writeable_outputs = [out for out in self.outputs if not out.closed]
        lines = message.split(self.line_separator)

        for out in writeable_outputs:
            out.write("%s%s" % (self.format(message), self.line_separator))
            out.flush()  # so tail output shows up immediately, for instance

    def cr(self):
        self.write(self.line_separator)

    def writecr(self, message):
        """Write the message, followed by the line separator, to all available
        outputs."""
        self.write(message)
        self.cr()

    def format(self, message):
        """Format the message using wrap_function, if any."""
        if self.wrap_function is not None:
            return self.line_separator.join(self.wrap_function(message))
        else:
            return message

    def trace(self, message):
        """Outputs a message only if self.debug is True."""
        if self.debug:
            self.write(message)


class ExplorationWriter(Writer):
    """Class which writes exploration-mode output."""

    def write_room(self, room, mode="brief"):
        """Write a room description using the current writer."""

        self.write(room.name)
        if hasattr(room, mode):
            self.write(getattr(room, mode))
        else:
            raise Exception("Game.write_room: invalid description level " % mode)
        self.write_exits(room)

    def write_exits(self, room):
        """Write out the room's exits using the current writer."""

        self.writecr("Exits: %s" % ", ".join(room.exits.keys()))
