# Classes which map user input to commands.

# Base class for reading and interpreting user input. Call next_command() to
# prompt for user input and convert it to a game logic method call.
# Interpreter classes should never have to do game logic, and game logic
# should never have to interpret strings.
# 
# The commands argument may be any object which has a patterns property; a
# patterns object must be a tuple or list of (pattern, command) tuples or
# lists. This pattern mapping will be used to match command names with command
# functions.
# 
# The command functions can come from anywhere, but will probably be
# references to methods on the commands object. The commands object is
# required to have the following commands: "command_not_found" and
# "command_is_whitespace".
class Interpreter
  def initialize(commands)
    @commands = commands
  end

  def read
    return process(gets)
  end

  # Convert the raw user input string into a form usable by interpret().
  # This implementation uses the default tokenize(), but subclasses may
  # override this, tokenize(), or both.
  def process(user_input)
    return tokenize(user_input)
  end

  # Naive string tokenization implementation: return a list of words, or
  # None if no string or an empty string was provided. Simply splits on
  # whitespace under the hood, after stripping leading and trailing
  # whitespace.
  def tokenize(string="")
    return string.strip.split
  end

  # Interpret the user input, ultimately calling a game logic command.
  # Subclasses probably do not have to override this method as long as they
  # implement read() and interpret().
  def next_command()
    interpret(read())
  end

  # Given a list of tokens, attempt to invoke the first token as a method of
  # the commands object using Object.send. Subclasses must implement; this
  # example implementation simply finds the base command by matching the first
  # argument, and executes it without further arguments.
  def interpret(tokens=nil)
    raise "#{self.class.name}#interpret(): no tokens provided." if tokens.nil?

    @commands.send tokens.first.to_sym
  end
end

class ExplorationInterpreter < Interpreter

end
