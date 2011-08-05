import textwrap


class Writer:
    """
    Base class for writing output.
    """

    def __init__(self, *args):
        self.outputs = list(args)
        self.wrap_function = textwrap.wrap  # default text wrap function
        self.line_separator = "\n"

    def write(self, message):
        """Write the message to all available outputs."""
        if len(self.outputs) == 0:
            raise "Writer.write: no outputs available"

        writeable_outputs = [out for out in self.outputs if not out.closed]
        for out in writeable_outputs:
            out.write("%s\n" % self.format(message))
            out.flush()  # so tail output shows up immediately, for instance

    def writecr(self, message):
        """Write the message, followed by the line separator, to all available
        outputs."""
        self.write("%s%s" % (message, self.line_separator))

    def format(self, message):
        """Format the message using wrap_function, if any."""
        if self.wrap_function is not None:
            return self.line_separator.join(self.wrap_function(message))
        else:
            return message
