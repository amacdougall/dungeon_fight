# Output classes which write to file-like objects.

# enable print statements to output without newlines
STDOUT.sync = true

# Base class for writing output. Default text width for wrapping purposes is 78
# columns. Alter this by setting Writer#columns. Alter the line separator by
# setting Writer#line_separator; default "\n".
class Writer
  attr_accessor :debug, :line_separator, :columns

  def initialize(*outputs)
    @outputs = outputs
    @columns = 78
    @line_separator = "\n"
    @debug = false
  end

  # Write the message to all available outputs, without text wrapping and
  # without a line separator. In other words, further writes should append to
  # the visual line.
  # TODO: separate output into classes to permit flexible formatting
  def write(message)
    raise "Writer.write: no outputs available" if @outputs.length == 0

    @outputs.reject(&:closed?).each do |out|
      out.write(format(message))
    end
  end

  # Print a line separator to all outputs.
  def linebreak
    @outputs.reject(&:closed?).each do |out|
      out.write @line_separator
    end
  end

  # Write the message to all available outputs. Use text wrapping and add a
  # line separator.
  def line(message)
    write(message)
    linebreak
  end

  # Write the message, with text wrapping, followed by two line separators, to
  # all available outputs. A convenience method equivalent to a line call
  # followed by a linebreak call. Visually, should create a space between the
  # message and whatever follows.
  def paragraph(message)
    line(message)
    linebreak
  end

  # Print a simple angle-bracket prompt, without a line separator. Subclasses
  # may override to provide status information or other data or decoration
  # along with the prompt.
  def prompt()
    write "> "
  end

  # Wraps the message at the specified column width.
  def wrap(message, col=78)
     wrapped = message.gsub(/(.{1,#{col}})( +|$\n?)|(.{1,#{col}})/, "\\1\\3\n").sub(/\n$/, "")
  end

  # Format the message using the wrap method, if any.
  # TODO: per-output format methods; or remove outputs in general to their own
  # writeable classes
  def format(message)
    wrap(message)
  end

  # Outputs a message only if @debug is true.
  def trace(message)
    write(message) if @debug
  end
end


# Class which writes exploration-mode output.
class ExplorationWriter < Writer
  # Write a room description.
  def write_room(room, mode=:brief)
    line(room.name)
    paragraph(room.send(mode)) unless room.send(mode).nil? # TODO: fallback?
    exits(room)
  end

  # Write out the room's exits using the current writer.
  def exits(room)
    line("Exits: #{room.exits.keys.join(", ")}")
  end
end
