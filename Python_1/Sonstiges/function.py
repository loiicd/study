data_set = [
            {"name" : "Max",
            "vehicle_type" : "A-Class",
            "mileage" : 1500000},
            {"name" : "Jona",
            "vehicle_type" : "S-Class",
            "mileage" : 23000},
            {"name" : "Jeff",
            "vehicle_type" : "G-Class",
            "mileage" : 10000},
            {"name" : "Joe",
            "vehicle_type" : "A-Class",
            "mileage" : 150000}]

# ------------------------------------
# --- Durchschnitt Milen Lösungs 1 ---
# ------------------------------------
def avg_mileage1(data_set: list) -> float:
  sum = 0
  for i in range(len(data_set)):
    sum += data_set[i]["mileage"]
  avg = sum / len(data_set)
  return avg
print(avg_mileage1(data_set))

# ------------------------------------
# --- Durchschnitt Milen Lösungs 2 ---
# ------------------------------------
def avg_mileage2(data_set: list) -> float:
  mileage_list = []
  for el in data_set:
    mileage_list.append(el["mileage"])
  return sum(mileage_list) / len(mileage_list)
print(avg_mileage2(data_set))


# ---------------------------------------
# --- Anzahl Fahrzeug Typen Lösungs 1 ---
# ---------------------------------------
def count_vehicle_type(data_set: list) -> dict:
  result_dic = {}
  for i in data_set:
    if i["vehicle_type"] in (result_dic.keys()):
      result_dic[i["vehicle_type"]] += 1
    else:
      result_dic[i["vehicle_type"]] = 1
  return result_dic


# ---------------------------------------
# ---------------------------------------
# ---------------------------------------
while True:
  value = input("Eingabe: ")
  if value == "avg_mileage1":
    print()
    print(avg_mileage1(data_set))
  elif value == "avg_mileage2":
    print()
    print(avg_mileage2(data_set))
  elif value == "count_vehicle_type":
    print()
    print(count_vehicle_type(data_set))