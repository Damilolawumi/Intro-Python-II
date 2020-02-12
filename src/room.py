# Implement a class to hold room information. This should have name and
# description attributes.
# The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
# which point to the room in that respective direction.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return "name: {}, description: {}, items: {}".format(self.name, self.description, self.items)    

    def add_item(self, item):
        self.items.append(item)    

    def remove_item(self, item):
        self.items.remove(item)    
