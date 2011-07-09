from input_reader import InputReader
from world.rooms import Map, Room
import json

reader = InputReader()

map_data = json.load(open("test_map.json"))

test_map = Map()

for room_data in map_data:
    room = Room(name=room_data["name"],
                brief=room_data["brief"],
                verbose=room_data["verbose"])
    room.exits = room_data["exits"]
    test_map.rooms[room.name] = room

# game loop
while command != "quit":
    command = reader.read()[0]
    here = test_map.move(command)
    if here is None:
        here = test_map.location
        print "There was no exit in the direction %s." % command
    else:
        print here.name
        print here.brief
