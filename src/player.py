# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room  
        self.inventory = []
        self.score = 0

    def __str__(self):
        return "name: {}, current room: {}, inventory: {}, score: {}".format(self.name, self.current_room, self.inventory, self.score)

    def grab_item(self, item):
        self.inventory.append(item)    

    def drop_item(self, item):
        self.inventory.remove(item)    