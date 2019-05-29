# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def move(self, direction):
            room_map = {
            'n': self.current_room.n_to,
            's': self.current_room.s_to,
            'e': self.current_room.e_to,
            'w': self.current_room.w_to}

            if room_map[direction] is None:
                print('There is nothing in that direction.')
            else: 
                self.current_room = room_map[direction]