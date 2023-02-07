import pandas as pd
import datetime as date

# clean sales codes
def clean_sales_codes(df: pd.DataFrame) -> pd.DataFrame:
  # change date format
  df['production_date'] = pd.to_datetime(df['production_date'], errors='coerce')

  # filter all dates higher than now and lower dan 1980
  df = df[df['production_date'] > date.datetime(1980, 1, 1, 0, 0, 0)]
  df = df[df['production_date'] < date.datetime.today()]

  # delete all empty rows
  df = df.dropna()

  return df

# clean vehicle hash
def clean_vehicle_hash(df: pd.DataFrame) -> pd.DataFrame:
  # delete all short fin
  df = df[df["fin"].str.len() > 16]

  # delete all empty rows
  df = df.dropna()

  df = df.drop(columns=["record_source", "load_ts"])

  return df


def most_countries(df: pd.DataFrame) -> pd.DataFrame:
  # filter all dates higher than xxx and lower dan xxx
  df = df[df['production_date'] > date.datetime(2017, 1, 1, 0, 0, 0)]
  df = df[df['production_date'] < date.datetime(2020, 12, 31, 0, 0, 0)]

  # drop all columns except country
  df = df.drop(df.columns.difference(['country']), 1)

  # alternate
  # df = df.drop(columns=["production_date", "sales_code_array", "fin"])

  # count Countries
  df = df.value_counts()

  # filter only the highest
  df = df.nlargest(3)

  return df


def highest_sell(df: pd.DataFrame) -> pd.DataFrame:
  # filter all dates higher than xxx and lower dan xxx
  df = df[df['production_date'] > date.datetime(2014, 1, 1, 0, 0, 0)]
  df = df[df['production_date'] < date.datetime(2020, 12, 31, 0, 0, 0)]

  df = pd.DatetimeIndex(df['production_date']).year

  df = df.value_counts()

  return df


def first_sell(df: pd.DataFrame) -> pd.DataFrame:
  df = df.nsmallest(1, "production_date")

  return df["fin"]


def vehicle_number_xxx(df: pd.DataFrame) -> pd.DataFrame:
  # filter all dates higher than xxx and lower dan xxx
  df = df[df['production_date'] > date.datetime(2017, 1, 1, 0, 0, 0)]
  df = df[df['production_date'] < date.datetime(2021, 1, 1, 0, 0, 0)]

  df = df.drop(columns=["production_date", "country"])
  dict = df.to_dict('records')

  return dict