# function for making the map
import helpers.variables as var
from random import randint
from Classes.Rect import Rect
from Classes.Entity import Entity
from helpers.create_room import create_room
from helpers.create_h_tunnel import create_h_tunnel
from helpers.create_v_tunnel import create_v_tunnel
from helpers.place_objects import place_objects
from helpers.send_to_back import send_to_back


def make_map():
    # create two rooms
    rooms = []
    num_rooms = 0

    for r in range(var.MAX_ROOMS):
        # random width and height
        w = randint(var.ROOM_MIN_SIZE, var.ROOM_MAX_SIZE)
        h = randint(var.ROOM_MIN_SIZE, var.ROOM_MAX_SIZE)
        # random position without going out of the boundaries of the map
        x = randint(0, var.MAP_WIDTH - w - 1)
        y = randint(0, var.MAP_HEIGHT - h - 1)

        # Rect class makes rectangles easier to work with
        new_room = Rect(x, y, w, h)

        # run through the other rooms and see if they intersect with this one
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # this means there are no intersections, so this room is valid
            # paint it to the map's tiles
            create_room(new_room)

            # center coordinates of new room, will be useful later
            (new_x, new_y) = new_room.center()

            # optional: print room number to see how the map drawing worked
            # room_no = Entity(new_x, new_y, chr(65 + num_rooms), 'white')
            # var.entities.insert(0, room_no)

            if num_rooms == 0:
                # this is the first room, where the player starts at
                var.player.x = new_x
                var.player.y = new_y
            else:
                # all rooms after the first:
                # connect it to the previous room with a tunnel
                # center coordinates of previous room
                (prev_x, prev_y) = rooms[num_rooms - 1].center()
                # draw a coin (random number that is either 0 or 1)
                if randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)

            # add some objects to the room, such as monterrs
            place_objects(new_room)
            # finally, append the new room to the list
            rooms.append(new_room)
            num_rooms += 1

            # create stairs at the center of the last room
            stairs = Entity(new_x, new_y, '<', 'white')
            var.entities.append(stairs)
            send_to_back(stairs)


