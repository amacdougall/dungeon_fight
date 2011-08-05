# Core game classes.
import yaml
from inputreader import ExplorationReader
from explore.rooms import Map, Room


class Game:
    """
    The core class which controls the game loops.

    Given map and party YAML, loads the player into the starting position.
    Handles the explore-combat loop cycle.
    """

    def __init__(self, map_filename, party_filename=None):
        """Initializes and starts the game."""

        print "map_filename is %s" % map_filename
        self.area = Map(yaml.load(open(map_filename)))
        # self.party = Party(yaml.load(open(party_filename)))
        print "Welcome to Dungeon Fight!" + "\n"
        print self.area.location.name + "\n"
        print "\n".join(textwrap.wrap(self.area.location.verbose))
        ExploreLoop(self)  # initialize with this game object
        print "Goodbye."


class ExploreLoop:
    """
    Handles the main exploration loop: movement, combat initiative."""

    def __init__(self, game):
        reader = ExplorationReader()
        command = reader.read()
        exit_commands = ["quit", "exit"]

        print "# initial command: %s" % command
        while not command in exit_commands:
            if command in ["l", "look"]:
                print game.area.location.name + "\n"
                print "\n".join(textwrap.wrap(game.area.location.verbose))
                print "Exits: %s" % ", ".join(game.area.location.exits.keys())
            elif command in ["i", "inv"]:
                print "Inventory is not yet implemented."
            else:
                # interpret as movement direction
                if game.area.move(command) is not None:
                    print game.area.location.name
                    print game.area.location.brief
                    print "Exits: %s" % ", ".join(game.area.location.exits.keys())
                else:
                    print "There is no exit in that direction.\n"
            command = reader.read()

if __name__ == "__main__":
    game = Game("test_map.yaml")
