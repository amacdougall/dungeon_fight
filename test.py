from input_reader import InputReader
from explore.rooms import Map, Room
import yaml
import textwrap

reader = InputReader()

map_data = yaml.load(open("test_map.yaml"))

test_map = Map()

for room_data in map_data["rooms"]:
    room = Room(name=room_data["name"],
                brief=room_data["brief"],
                verbose=room_data["verbose"])
    room.exits = room_data["exits"]
    test_map.rooms[room.name] = room

test_map.location = test_map.rooms[map_data["starting_room"]]

# game loop
here = test_map.location
command = None

# print startup messages
print "Welcome to Dungeon Fight!"
print
print here.name
print "\n".join(textwrap.wrap(here.verbose))
print "Exits: %s" % ", ".join(here.exits.keys())

# TODO: this, only better
while not command in ["quit", "exit", "q"]:
    command = reader.read()[0]
    if command in ["quit", "exit", "q"]:
        break

    if command == "l":
        print here.name
        print "\n".join(textwrap.wrap(here.verbose))
        print "Exits: %s" % ", ".join(here.exits.keys())
        continue

    here = test_map.move(command)
    if here is None:
        here = test_map.location
        print "There was no exit in the direction %s." % command
    else:
        print here.name
        print here.brief
        print "Exits: %s" % ", ".join(here.exits.keys())

print "bye"
