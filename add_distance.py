import pandas as pd
import numpy as np


def calc(coords):
    coords["start_lat"] = np.radians(coords["start_lat"])
    coords["start_lng"] = np.radians(coords["start_lng"])
    coords["end_lat"] = np.radians(coords["end_lat"])
    coords["end_lng"] = np.radians(coords["end_lng"])
    coords["dlat"] = coords["end_lat"] - coords["start_lat"]
    coords["dlng"] = coords["end_lng"] - coords["start_lng"]
    coords["a"] = np.sin(coords["dlat"] / 2)**2 + np.cos(coords["start_lat"]) * np.cos(coords["end_lat"]) * np.sin(coords["dlng"] / 2)**2
    coords["c"] = 2 * np.asin(np.sqrt(coords["a"]))
    coords["distance"] = coords["c"] * 6371
    return coords["distance"]


df = pd.read_csv("datasets/tripdata-2018.csv")

df["stations_dist"] = calc(df[["start_lat", "start_lng", "end_lat", "end_lng"]])
df["fact_dist"]
print(df)