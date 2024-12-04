import pandas as pd #type: ignore
import numpy as np #type: ignore
import math


def add_cost(x):
    if x[0] == "casual":
        final_cost = 9.95

        if x[1] > 30: final_cost += 2
        if x[1] > 60: final_cost += 6
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 8

        return final_cost
    
    else:
        final_cost = 0.0

        if x[1] > 30: final_cost += 1.5
        if x[1] > 60: final_cost += 4.5
        if x[1] > 90:
            final_cost += math.floor((x[1] - 90) / 30) * 6

        return final_cost


df = pd.read_csv("datasets/tripdata-2016.csv")
df_copy = df.copy()
df_copy = df_copy.apply(lambda row: [row["member_casual"]] + [row["duration"]], axis=1)

df["cost"] = df_copy.map(add_cost)

print(df.head(15))

df.reset_index().set_index("ride_id").drop('index', axis=1).to_csv("datasets/tripdata-2016.csv")
del df, df_copy