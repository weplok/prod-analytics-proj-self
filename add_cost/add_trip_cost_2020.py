import pandas as pd #type: ignore
import numpy as np #type: ignore
import math


def add_cost(x):
    if x[2] != "electric_bike":
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15

                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.15

                return final_cost
            else:
                final_cost = 3

                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.15

                return final_cost

        else:
            final_cost = 0

            if x[1] >= 45:
                final_cost += (round(x[1]) - 45) * 0.15

            return final_cost
    else:
        if x[0] == "casual":
            if x[1] > 45:
                final_cost = 15

                if x[1] > 180:
                    final_cost += (round(x[1]) - 180) * 0.20

                return final_cost
            else:
                final_cost = 3

                if x[1] > 30:
                    final_cost += (round(x[1]) - 30) * 0.20

                return final_cost

        else:
            final_cost = 0

            if x[1] >= 45: 
                final_cost += (round(x[1]) - 45) * 0.15

            return final_cost


df = pd.read_csv("datasets/tripdata-2020.csv")
df_copy = df.copy()
df_copy = df_copy.apply(lambda row: [row["member_casual"]] + [row["duration"]] + [row["rideable_type"]], axis=1)

df["cost"] = df_copy.map(add_cost)

print(df.head(15))

df.reset_index().set_index("ride_id").drop('index', axis=1).to_csv("datasets/tripdata-2020.csv")
del df, df_copy