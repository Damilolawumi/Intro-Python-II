from room import Room
from player import Player
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
chamber! The only exit is to the south."""),
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

room['outside'].add_item(Item("key", "used to open doors"))
room['foyer'].add_item(Item("sword", "used to slay monsters"))
room['overlook'].add_item(Item("coins", "used to buy swords"))
room['narrow'].add_item(Item("gem", "precious jewel"))
room['treasure'].add_item(Item("treasure", "contains lots of precious jewels and coins"))

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

def start_game():
    print("*" * 20)
    print("Welcome to my adventure game!")
    print("Navigate through all areas of the game and try to find the hidden treasure. \nBonus points for picking up objects along the way.\n")
    print('Please enter the name of your player: ')
    name = input()
    global player 
    player = Player(name, room['outside'])
    print("*" * 20)

def display_current_position_and_items():
    print(f'Player: \n{player.name}\n')
    print(f'Your current position: \n{player.current_room.name}\n')
    print(f'Clue: \n{player.current_room.description}\n')
    print('Room Items:')
    for item in player.current_room.items:
        print(f'{item.name.capitalize()} : {item.description}')
    print('\nInventory:')
    for item in player.inventory:
        print(f'{item.name.capitalize()} : {item.description}')

def move_player():
    print("\nSelect a direction to move in: ")
    for (key, value) in direction_options.items():
        print(f'[{key}] : {value}')
    selection = input()    
    if selection.lower() in direction_options:
        if getattr(player.current_room, f'{selection.lower()}_to') != None:
            player.current_room = getattr(player.current_room, f'{selection.lower()}_to')
        else:
            print("\nYou have reached a dead end :( Try turning back the way you came!") 
    else: 
        print("\nOops! Not a valid direction. Please try again.")    

def grab_item(item):
    for obj in player.current_room.items:
        if obj.name == item:
            player.current_room.remove_item(obj)
            player.grab_item(obj)
            print(obj.on_take())
        else:
            print(f'Oops! {player.current_room.name} does not contain {item}. Try again.')  

def drop_item(item):
    for obj in player.inventory:
        if obj.name == item:
            player.drop_item(obj)
            player.current_room.add_item(obj)
            print(obj.on_drop())
        else:
            print(f'Oops! Your inventory does not contain {item}. Try again.')    

def play():
    if selection == 'm':
        move_player()  
    elif selection[:4] == 'grab' or selection[:4] == 'drop':
        action = selection[:4]
        obj = selection[5:]
        if action == 'grab':
            grab_item(obj)
        elif action == 'drop':   
            drop_item(obj)
    else:
        print(f'Oops! not a valid game option. Try again')
    

selection = ""

player = None

quit_game = False

direction_options = {
    'n' : 'North',
    's' : 'South',
    'e' : 'East',
    'w' : 'West'
}

game_options = {
    'drop + item' : 'Drop an item in your inventory',
    'grab + item' : 'Grab an item in the current room',
    'm' : 'Move to a different room',
    'q' : 'Quit game'
}

start_game()
while quit_game == False and player != None:
    print("*" * 20)
    display_current_position_and_items()
    print("\nWhat would you like to do?")
    for (key, value) in game_options.items():
        print(f'[{key}] : {value}')
    print("*" * 20) 
    selection = input()
    if selection == 'q':
       print(f'\nThank you for playing, {player.name}. Goodbye!')
       quit_game = True
    else:
       play()      