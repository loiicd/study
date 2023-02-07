from classes import *
from definitions import *

specials = {111: ["Badenwanne", 20], 112: ["Pool", 40]}

rooms =[Room("N001", 2, [], True, []), 
        Room("N002", 1, [], True, []),
        Room("N003", 2, [], True, []),
        Room("N004", 2, [], True, []),
        Room("N005", 1, [], True, [112]),
        Room("N006", 1, [], True, [111]),
        Room("N007", 1, [], True, [111]),
        Room("N008", 2, [], True, [112]),
        Room("N009", 2, [], True, [])
      ] 

guests = []

while True:
  print()
  input_value = input("Eingabe: ").lower()
  match input_value:

    # ***************
    # *** Checkin ***
    # ***************
    case "checkin":
      firstname = input("Firstname: ")
      lastname = input("Lastname: ")
      budget = int(input("Budget: "))

      checkRooms(rooms, budget)
      
      print()
      room = input("Room: ")

      saveGuest(firstname, lastname, budget, guests)
      # checkin(firstname, lastname, budget, guests, rooms, room)

    # *********************
    # *** Create Guests ***
    # *********************
    case "create guest":
      print()
      firstname = input("Firstname: ")
      lastname = input("Lastname: ")
      budget = int(input("Budget: "))

      print(saveGuest(firstname, lastname, budget, guests))

    # ******************
    # *** Show Rooms ***
    # ******************
    case "show rooms":
      print()
      print("*******************")
      for room in rooms:
        print(f"{room.number} - Beds: {room.beds} Guests: {room.guests} Cleaned: {room.cleaned}")
      print("*******************")

    # ************************
    # *** Show Empty Rooms ***
    # ************************
    case "show empty rooms":
      emptyRooms = getEmptyRooms(rooms)
      print()
      print("*****************************")
      for room in emptyRooms:
        print(f"{room.number} - Beds: {room.beds} Cleaned: {room.cleaned}")
      print("*****************************")

    # *******************
    # *** Show Guests ***
    # *******************
    case "show guests":
      print()
      print("*****************************")
      for guest in guests:
        print(f"{guest.firstname} {guest.lastname} - Budget: {guest.budget}")
      print("*****************************")

    # ********************
    # *** End Programm ***
    # ********************
    case "break":
      print()
      print("#################")
      print("Closing Programm!")
      print("#################")
      break

    # *********************
    # *** Wrong Command ***
    # *********************
    case other:
      print()
      print("##################")
      print("Command not exist!")
      print("##################")