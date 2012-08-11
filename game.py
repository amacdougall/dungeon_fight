# Core game classes.
import sys
import yaml
from input import InputReader
from output import ExplorationWriter
from interpreter import ExplorationInterpreter
from explore.rooms import Map, Room


class Game(object):
    """
    The core class which controls the game loops.

    Given map and party YAML, loads the player into the starting position.
    Handles the explore-combat loop cycle.
    """

    def __init__(self, map_filename, party_filename=None):
        """Initializes and starts the game."""
        self.exit_requested = False

        self.writer = ExplorationWriter(sys.stdout)  # TODO: writer switching
        self.writer.writecr("map_filename is %s" % map_filename)
        self.area = Map(yaml.load(open(map_filename)))
        self.writer.writecr("Welcome to Dungeon Fight!")
        self.writer.write_room(self.area.location, "verbose")

        ExploreLoop(self)  # initialize with this game object

        self.writer.writecr("Goodbye.")

    # EXPLORATION COMMANDS
    def look(self, arguments=None):
        self.writer.write_room(self.area.location, "verbose")

    def inventory(self, arguments=None):
        self.writer.writecr("Inventory is not yet implemented.")

    def wait(self, arguments=None):
        self.writer.writecr("Time passes.")

    def move_command(self, direction):
        def command(arguments=None):
            if self.area.move(direction) is not None:
                self.writer.write_room(self.area.location)
            else:
                self.writer.writecr("There is no exit in this direction.")

        return command

    def exit(self, arguments=None):
        self.exit_requested = True

    # COMBAT COMMANDS
    def fight(self, arguments=None):
        """Placeholder combat command."""
        pass


class ExploreLoop(object):
    """
    Handles the main exploration loop: movement, combat initiative. This loop
    may invoke secondary loops such as inventory, combat.
    """

    def __init__(self, game):
        reader = InputReader(game)
        interpreter = ExplorationInterpreter(game)

        while not game.exit_requested:
            command = reader.read()
            interpreter.interpret(command)


if __name__ == "__main__":
    game = Game("test_map.yaml")
