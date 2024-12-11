import pandas as pd


first_df = pd.read_csv(f"mdatasets/tripdata-2013.csv")
first_df = first_df.reset_index().set_index("ride_id").drop('index', axis=1)
first_df.to_csv("mdatasets/tripdata-full.csv")
del first_df

for year in range(2014, 2025):
    df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
    df = df.reset_index().set_index("ride_id").drop('index', axis=1)
    df.to_csv("mdatasets/tripdata-full.csv", mode="a", header=False)
    del df
