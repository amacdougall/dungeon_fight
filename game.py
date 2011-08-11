# Core game classes.
import sys
import yaml
from input import ExplorationReader
from output import ExplorationWriter
from explore.rooms import Map, Room


class Game:
    """
    The core class which controls the game loops.

    Given map and party YAML, loads the player into the starting position.
    Handles the explore-combat loop cycle.
    """

    def __init__(self, map_filename, party_filename=None):
        """Initializes and starts the game."""

        self.writer = ExplorationWriter(sys.stdout)  # TODO: writer switching
        self.writer.writecr("map_filename is %s" % map_filename)
        self.area = Map(yaml.load(open(map_filename)))
        # self.party = Party(yaml.load(open(party_filename)))
        self.writer.writecr("Welcome to Dungeon Fight!")
        self.writer.write_room(self.area.location, "verbose")

        ExploreLoop(self)  # initialize with this game object

        self.writer.writecr("Goodbye.")


class ExploreLoop:
    """Handles the main exploration loop: movement, combat initiative."""

    def __init__(self, game):
        reader = ExplorationReader()
        command = reader.read()
        exit_commands = ["quit", "exit"]

        while not command in exit_commands:
            if command in ["l", "look"]:
                game.writer.write_room(game.area.location, "verbose")
            elif command in ["i", "inv"]:
                game.writer.writecr("Inventory is not yet implemented.")
            else:
                # interpret as movement direction
                if game.area.move(command) is not None:
                    game.writer.write_room(game.area.location)
                else:
                    game.writer.writecr("There is no exit in that direction.\n")
            command = reader.read()

if __name__ == "__main__":
    game = Game("test_map.yaml")
