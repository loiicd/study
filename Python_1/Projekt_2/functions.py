from basic_functions import *

# ----------------
# --- AVG Mile ---
# ----------------
def avg_mileage_old(data: list[dict], vehicle_type: str = "") -> float:
  mileage_list = []
  if not vehicle_type:
    mileage_list = [el["mileage"] for el in data]
  else:
    for el in data:
      if el["vehicle_type"] == vehicle_type:
        mileage_list.append(el["mileage"])
  return avg(mileage_list)

# ----------
def avg_mileage(**kwargs) -> float:
  vehicle_type = ""
  for key, value in kwargs.items():
    if key == "data":
      data = value
    elif key == "vehicle_type":
      vehicle_type = value
    else:
      print(f"{key} is not a valid key")
  mileage_list = []
  if not vehicle_type:
    mileage_list = [el["mileage"] for el in data]
  else:
    for el in data:
      if el["vehicle_type"] == vehicle_type:
        mileage_list.append(el["mileage"])
  return avg(mileage_list)





# ------------------------
# --- Vehicler Counter ---
# ------------------------
def count_vehicle_type(data: list[dict]) -> dict:
  result_dic = {}
  for i in data:
    if i["vehicle_type"] in (result_dic.keys()):
      result_dic[i["vehicle_type"]] += 1
    else:
      result_dic[i["vehicle_type"]] = 1
  return result_dic

# -----------------------
# --- AVG Damage Cost ---
# -----------------------
def avg_damage_cost(data: list[dict]) -> float:
  costs = []
  for i in range(len(data)):
    costs.append(data[i]["damage"]["cost"])
  avg = sum(costs) / len(costs)
  return avg

# ---------------------------
# --- Most Damage Type ---
# ---------------------------+
def highest_damage_type(data: list[dict]) -> float:
  result_dic = {}
  for i in data:
    if i["damage"]["type"] in (result_dic.keys()):
      result_dic[i]["damage"]["type"] += 1
    else:
      result_dic[i]["damage"]["type"] = 1
  
  max_value = 0
  for key, value in result_dic.items():
    if value > max_value:
      max_value = value
  return key

