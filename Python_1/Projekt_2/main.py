import functions as f
import workshop_data as wd

while True:
  input_value = input("Eingabe: ")

  match input_value:
    case "1":
      # print(f.avg_mileage(wd.data))
      print(f.avg_mileage(data = wd.data, vehicle_type = "S-Class"))
    case "2":
      print(f.count_vehicle_type(wd.data))
    case "3":
      print(f.avg_damage_cost(wd.data))
    case "4":
      print(f.highest_damage_type(wd.data))
