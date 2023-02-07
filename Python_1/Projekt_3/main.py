import json

f = open("/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python/Projekt_3/workshop_data.json", "r")
data = json.load(f)

print(data)