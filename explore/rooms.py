# Classes defining rooms in the world model.


class Map(object):
    """A map of the world, or at least an area."""
    def __init__(self, data=None):
        self.rooms = {}
        self.location = None  # current room

        if data is not None:
            for room_data in data["rooms"]:
                room = Room(name=room_data["name"],
                            brief=room_data["brief"],
                            verbose=room_data["verbose"])
                room.exits = room_data["exits"]
                self.rooms[room.name] = room

            self.location = self.rooms[data["starting_room"]]


    def move(self, direction):
        """Move in the direction, if possible. Return new location, or None."""
        if not direction in self.location.exits:
            return None
        destination = self.location.exits[direction]
        if not destination in self.rooms:
            raise "%s was not a known room name." % destination
        self.location = self.rooms[destination]
        return self.location


class Room(object):
    """A simple room within the world."""
    def __init__(self, **kwargs):
        self.name = kwargs["name"] if "name" in kwargs else None
        self.verbose = kwargs["verbose"] if "verbose" in kwargs else None
        self.brief = kwargs["brief"] if "brief" in kwargs else None
        self.items = []  # items lying in the room
        self.exits = {}  # direction->room_name pairs
