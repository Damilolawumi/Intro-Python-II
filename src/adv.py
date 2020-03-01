from player import Player
from room import Room
from item import Item

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
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player('Damilola', room['outside'])

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

path = ''

error = "Sorry, you can not go in that direction please chose n, w, e or s"

while True:
    print(f'welcome {player.name} to this amazing adventure.\nYou are currently in the {player.current_room} ')
    path = input(f'Please choose a direction to start: n, w, e or s\n')
    current_room = player.current_room

    if path == 'n':
        print(f'You chose the north .... Good choice')
        next_room = player.current_room.n_to
        player.move_the_player(next_room)

    elif path == 's':
        print(f"You chose south...Thats really amazing")
        next_room = player.current_room.s_to
        player.move_the_player(next_room)  
 
                  
    elif path == 'w':
        print(f'You chose west...Thats not weird at all')
        next_room = player.current_room.w_to
        player.move_the_player(next_room)

    elif path == 'e':
        print(f"You chose east...cooool move")
        next_room = player.current_room.e_to
        player.move_the_player(next_room)

    
    elif path == 'q':
        print(f"oops... You have decided to quit the game.")
        break

    else:
        print(error)          