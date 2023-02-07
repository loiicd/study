import pandas as pd
import matplotlib.pyplot as plt
from functions import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Load all Excel Sheets
df_sales_codes = pd.read_excel(r'/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python_1/Praxisprojekt/vehicle_data.xlsx', sheet_name='sales_codes')
df_vehicle_hash = pd.read_excel(r'/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python_1/Praxisprojekt/vehicle_data.xlsx', sheet_name='vehicle_hash')
df_engines = pd.read_excel(r'/Users/loicdoerr/Library/Mobile Documents/com~apple~CloudDocs/Development/DHBW/Python_1/Praxisprojekt/vehicle_data.xlsx', sheet_name='engines')

# Clean Data Frames
df_sales_codes = clean_sales_codes(df_sales_codes)
df_vehicle_hash = clean_vehicle_hash(df_vehicle_hash)

# Merge Data Frame (sales_codes, vehicle_hash)
df = df_sales_codes.merge(df_vehicle_hash[["h_vehicle_hash", "fin"]])

# Drop unusable columns
df = df.drop(columns=["Unnamed: 0", "h_vehicle_hash"])

# print(vehicle_number_xxx(df))

# print(df)


# Count countries
most_countries(df).plot.bar()
plt.show()

# Count highest cell
highest_sell(df).plot.bar()
plt.show()

print(f"First vehicle sell: {first_sell(df)}")


