from classes import *


# ***********************
# *** Get Empty Rooms ***
# ***********************
def getEmptyRooms(rooms: list, budget: int = None):
  emptyRooms = []
  for room in rooms:
    if len(room.guests) == 0:
      if budget != None:
        if budget > room.beds * 220:
          emptyRooms.append(room)
      else: 
        emptyRooms.append(room)
    
  return emptyRooms


# ******************
# *** Save Guest ***
# ******************
def saveGuest(firstname: str, lastname: str, budget: float, guests: list):
  if (guests.append(Guest(firstname, lastname, budget))):
    return "Guest added succesfull!"

# *****************
# *** Book Room ***
# *****************
def bookRoom():
  pass
