# Core game classes.
import sys
import yaml
from input import ExplorationReader
from output import Writer
from explore.rooms import Map, Room


class Game:
    """
    The core class which controls the game loops.

    Given map and party YAML, loads the player into the starting position.
    Handles the explore-combat loop cycle.
    """

    def __init__(self, map_filename, party_filename=None):
        """Initializes and starts the game."""

        self.writer = Writer(sys.stdout)
        self.writer.writecr("map_filename is %s" % map_filename)
        self.area = Map(yaml.load(open(map_filename)))
        # self.party = Party(yaml.load(open(party_filename)))
        self.writer.writecr("Welcome to Dungeon Fight!")
        self.write_room(self.area.location, "verbose")

        ExploreLoop(self)  # initialize with this game object

        self.writer.writecr("Goodbye.")

    def write_room(self, room, mode="brief"):
        """Write a room description using the current writer."""
        # TODO: find a better place for this; ExplorationWriter?
        self.writer.write(room.name)
        if hasattr(room, mode):
            self.writer.write(getattr(room, mode))
        else:
            raise Exception("Game.write_room: invalid description level " % mode)
        self.write_exits(room)

    def write_exits(self, room):
        """Write out the room's exits using the current writer."""
        # TODO: definitely needs its own class
        self.writer.writecr("Exits: %s" % ", ".join(room.exits.keys()))


class ExploreLoop:
    """Handles the main exploration loop: movement, combat initiative."""

    def __init__(self, game):
        reader = ExplorationReader()
        command = reader.read()
        exit_commands = ["quit", "exit"]

        while not command in exit_commands:
            if command in ["l", "look"]:
                game.write_room(game.area.location, "verbose")
            elif command in ["i", "inv"]:
                print "Inventory is not yet implemented."
            else:
                # interpret as movement direction
                if game.area.move(command) is not None:
                    game.write_room(game.area.location)
                else:
                    print "There is no exit in that direction.\n"
            command = reader.read()

if __name__ == "__main__":
    game = Game("test_map.yaml")
