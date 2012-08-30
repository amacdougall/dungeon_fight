# Classes defining rooms in the world model.
require 'pry'
require 'pry-nav'


# A map of the world, or at least an area.
class Map
  attr_accessor :location

  def initialize(data=nil)
    @rooms = {}
    @location = nil  # current room

    if data != nil
      data["rooms"].each do |room_data|
        room = Room.new(:name => room_data["name"],
                        :brief => room_data["brief"],
                        :verbose => room_data["verbose"])
        room.exits = room_data["exits"]
        @rooms[room.name] = room
      end

      @location = @rooms[data["starting_room"]]
    end
  end

  # Move in the direction, if possible. Return new location, or None.
  def move(direction)
    if not @location.exits.include? direction
      return nil
    end
    destination = @location.exits[direction]
    if not @rooms.include? destination 
      raise "%s was not a known room name." % destination
    end
    @location = @rooms[destination]
    return @location
  end
end


# A simple room within the world.
class Room
  attr_accessor :name, :verbose, :brief, :items, :exits

  def initialize(properties)
    @name = properties[:name]
    @verbose = properties[:verbose]
    @brief = properties[:brief]
    @items = []  # items lying in the room
    @exits = {}  # direction->room_name pairs
  end
end
