# Output classes which write to file-like objects.


# Base class for writing output.
class Writer
  attr_accessor :debug, :line_separator

  def initialize(*outputs)
    @outputs = outputs
    # TODO: get wrap function
    @line_separator = "\n"
    @debug = false
  end

  # Write the message to all available outputs.
  def write(message)
    raise "Writer.write: no outputs available" if @outputs.length == 0

    writeable_outputs = @outputs.reject(&:closed?)
    # TODO: something with the following?
    lines = message.split(@line_separator)

    writeable_outputs.each do |out|
      # TODO: format
      out.write("#{message}#{@line_separator}")
    end
  end

  def cr
    write(@line_separator)
  end

  # Write the message, followed by the line separator, to all available outputs.
  def writecr(message)
    write(message)
    cr()
  end

  # Print a simple angle-bracket prompt. Subclasses may override to provide
  # status information or other data or decoration along with the prompt.
  def prompt()
    write "> "
  end

  # Format the message using wrap_function, if any.
  # TODO: this, but in Ruby
  # def format(self, message):
  #     if self.wrap_function is not None:
  #         return self.line_separator.join(self.wrap_function(message))
  #     else:
  #         return message

  # Outputs a message only if @debug is true.
  def trace(message)
    write(message) if @debug
  end
end


# Class which writes exploration-mode output.
class ExplorationWriter < Writer
  # Write a room description.
  def write_room(room, mode=:brief)
    write(room.name)
    write(room.send(mode)) unless room.send(mode).nil? # TODO: fallback?
    write_exits(room)
  end

  # Write out the room's exits using the current writer.
  def write_exits(room)
    writecr("Exits: #{room.exits.keys.join(", ")}")
  end
end
