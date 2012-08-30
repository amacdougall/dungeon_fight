require 'yaml'
require './interpreter'
require './commands'
require './output'
require './map'


# enable print statements to output without newlines
STDOUT.sync = true

# The core class which controls the game loops.
# 
# Given map and party YAML, loads the player into the starting position.
# Handles the explore-combat loop cycle.
class Game
  attr_accessor :writer, :area, :exit_requested

  def initialize(map_filename, party_filename = nil)
    @exit_requested = false

    @writer = ExplorationWriter.new(STDOUT)
    @writer.writecr("map_filename is %s" % map_filename)
    @area = Map.new(YAML.load(File.read(map_filename)))
    @writer.writecr("Welcome to Dungeon Fight!")
    @writer.write_room(@area.location, "verbose")

    ExploreLoop.new(self)  # initialize with this game object

    @writer.writecr("Goodbye.")
  end
end


# Handles the main exploration loop: movement, combat initiative. This loop
# may invoke secondary loops such as inventory, combat.
class ExploreLoop
  def initialize(game)
    interpreter = ExplorationInterpreter.new(ExplorationCommands.new(game))
    while not game.exit_requested
      game.writer.prompt()
      interpreter.next_command()
    end
  end
end

game = Game.new("test_map.yaml")
