import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 10)

# read data
df_supermarket_sales = pd.read_csv("supermarket_sales.csv")

# explore data
# print(df_supermarket_sales.columns)
# print(df_supermarket_sales.head())

# print(df_supermarket_sales)

# x = df_supermarket_sales.groupby(["Branch", "Gender"]).columns
x = df_supermarket_sales.columns
y = df_supermarket_sales.groupby(["Branch", "Gender"])["Invoice ID"].count()

df_supermarket_sales.groupby(["Branch", "Gender"])["Invoice ID"].count().plot(kind="bar")

plt.xticks(rotation=0, horizontalalignment="center")
plt.xlabel("Gender by Branch")
plt.ylabel("Amount")
plt.show()