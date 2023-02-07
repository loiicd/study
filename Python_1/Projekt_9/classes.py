class Room:
  def __init__(self, number: str, beds: int, specials: list, cleaned: bool, guests: list):
    self.number = number
    self.beds = beds
    self.specials = specials
    self.cleaned = cleaned
    self.guests = guests

class Guest:
  def __init__(self, firstname: str, lastname: str, budget: float):
    self.firstname = firstname
    self.lastname = lastname
    self.budget = budget


def checkRooms(rooms: list, budget: int):
  print()
  print("Empty Rooms:")
  print("*******************")
  for room in rooms:
    if len(room.guests) == 0:
      if budget > room.beds * 220:
        print(f"{room.number} - Betten: {room.beds}")
  print("*******************")


def checkin(firstname: str, lastname: str, budget: float, guests: list, rooms: list, room: str):
  guest = guests.append(Guest(firstname, lastname, budget))
  for rr in rooms:
    if rr.number == room:
      rr.guests.append(guest)