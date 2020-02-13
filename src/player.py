# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
      # attributes (name, categories)
    self.name = name
    self.current_room = current_room

  def move_the_player(self, room):
        if room != None:
            self.set_the_player_room(room)
        else:
            print("-->Sorry, you cannot move in this direction in your current room<--")  

  def set_the_player_room(self, room):
        self.current_room = room

  def __str__(self):
    return f"{self.name} is currently in {self.current_room}"



  