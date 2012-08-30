# Core module containing all commands which can be invoked by user input. Pass
# these classes as parameters to Interpreter class constructors.


# All commands used in exploration mode.
class ExplorationCommands
  def initialize(game)
    @game = game
  end

  def method_missing(symbol, *args)
    case symbol
      when /(quit|exit)$/ then       quit
      when /l(ook)?$/ then           look
      when /i(nv(entory)?)?$/ then   inventory
      when /e(ast)?$/ then           move "e"
      when /w(est)?$/ then           move "w"
      when /n(orth)?$/ then          move "n"
      when /s(outh)?$/ then          move "s"
      when /up?$/ then               move "u"
      when /d(own)?$/ then           move "d"
      when /(z|wait)$/ then          wait
    end
  end

  # TODO: I imagine there is still a better way; I'd like to keep the routing
  # concept, but do something more Rubyish
  private
  def look
    @game.writer.write_room(@game.area.location, "verbose")
  end

  def inventory
    @game.writer.writecr("Inventory is not yet implemented.")
  end

  def wait
    @game.writer.writecr("Time passes.")
  end

  def move(direction)
    if not @game.area.move(direction).nil?
      @game.writer.write_room(@game.area.location)
    else
      @game.writer.writecr("There is no exit in this direction.")
    end
  end

  def quit
    @game.exit_requested = true
  end
end
