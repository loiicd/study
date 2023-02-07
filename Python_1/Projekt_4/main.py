import json

class Vehicle:
  def __init__(self, color : str, brand : str, engine : str, max_speed : int, seats : int, weight : int):
    self.color = color
    self.brand = brand
    self.engine = engine
    self.max_speed = max_speed
    self.seats = seats
    self.weight = weight

  def print_info(self):
    print(f"Brand: {self.brand}")
    print(f"Color {self.color}")
    print(f"engine: {self.engine}")
    print(f"Speed: {self.max_speed}")
    print(f"Seats: {self.seats}")
    print(f"Weight: {self.weight}")

  def update_speed(self, max_speed : int):
    self.max_speed = max_speed

class Garage:
  def __init__(self, capacity : int, alarm : bool, fleet : list[Vehicle]):
    if capacity < len(fleet):
      self.fleet = fleet[0:capacity]
      print()
      print("***********************************")
      print("ERROR - To many vehicles in garage!")
      print("***********************************")
    else:
      self.fleet = fleet
    self.capacity = capacity
    self.alarm = alarm

  def print_fleet(self):
    print()
    print("Garage:")
    for car in self.fleet:
      print("----------")
      car.print_info()

class Dashboard:
  def __init__(self):
    self.number_vehicles = len(fleet)
    self.avg_weight = sum(fleet) / len(fleet)
    self.number_vehicles_per_brand = count_vehicle_type(fleet)

  def print_dashboard(self):
    print(f"Vehicles: {self.number_vehicles}")
    print(f"avg Weight: {self.avg_weight}")
    print(f"Vehicles per Brand: {self.number_vehicles_per_brand}")

def count_vehicle_type(data: list[dict]) -> dict:
  result_dic = {}
  for i in data:
    if i["vehicle_type"] in (result_dic.keys()):
      result_dic[i["vehicle_type"]] += 1
    else:
      result_dic[i["vehicle_type"]] = 1
  return result_dic


file = open("/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python/Projekt_4/vehicle_data.json", "r")
vehicle_data = json.load(file)

fleet = []
for car in vehicle_data:
  fleet.append(Vehicle(color = car["color"], brand = car["vehicle_brand"], engine = car["engine"]["cylinder"], max_speed = car["engine"]["max_speed"], seats = car["seats"], weight = car["weight"], ))


my_garage = Garage(capacity = 5, alarm = False, fleet = fleet)

my_garage.print_fleet()

