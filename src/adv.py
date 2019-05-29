from room import Room
import sys
from player import Player
from item import Item
import textwrap 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add some items
room['foyer'].add_item(Item('Greatsword',"Like the good sword, but better"))
room['foyer'].add_item(Item('Morningstar',"A spiky ball of iron on a stick"))

# Printing function for long descriptions, with text wrapping
def print_description(desc):
    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=desc) 
    for element in word_list: 
        print(element) 
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.




# Intro message
print("\n<< Welcome to The Adventure Game. >>\n")
print('Enter cardinal directions to move, or any other key to exit the game.')

# Initialize player
name = input("What is your name, traveler? ")
player = Player(name=name, starting_room=room['outside'])
print(f"\nWelcome, {name}")
print(f"\nCurrent location: {player.current_room.name}.")
print("\nYou see the following items:")
player.current_room.print_items()

# Initialize input loop
direction = input("\nWhich direction do you move? (n, s, e, or w) ")

# Input loop that updates the current room using usir inputs. Any input
# other than the cardinal directions exits the program.
while direction in ['n', 's', 'e', 'w']:
    print('-------------------------------')
    prev_room = player.current_room
    player.move(direction)
    
    # Tell the user which way they went, but only if they changed rooms
    if player.current_room != prev_room:
        print(f"\nYou move into: {player.current_room.name}\n")
        print_description(player.current_room.description)
        print("\nYou see the following items:")
        player.current_room.print_items()
    
    direction = input("\nWhich direction do you move? (n, s, e, or w) ")
