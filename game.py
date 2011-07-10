# Core game classes.


class Game:
    """
    The core class which controls the game loops.

    Given map and party YAML, loads the player into the starting position.
    Handles the explore-combat loop cycle.
    """

    def __init__(self, map_filename, party_filename):
        """Initializes and starts the game."""

        map_file = open(map_filename)
        party_file = open(party_filename)
