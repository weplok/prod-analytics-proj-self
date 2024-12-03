import pandas as pd
import numpy as np


def stations_dist(coords):
    coords["start_lat"] = np.radians(coords["start_lat"])
    coords["start_lng"] = np.radians(coords["start_lng"])
    coords["end_lat"] = np.radians(coords["end_lat"])
    coords["end_lng"] = np.radians(coords["end_lng"])

    coords["dlat1"] = coords["start_lat"] - coords["start_lat"]
    coords["dlng1"] = coords["end_lng"] - coords["start_lng"]
    coords["a1"] = np.sin(coords["dlat1"] / 2) ** 2 + np.cos(coords["start_lat"]) * np.cos(
        coords["start_lat"]) * np.sin(coords["dlng1"] / 2) ** 2
    coords["c1"] = 2 * np.arcsin(np.sqrt(coords["a1"]))
    coords["distance1"] = coords["c1"] * 6371

    coords["dlat2"] = coords["end_lat"] - coords["start_lat"]
    coords["dlng2"] = coords["end_lng"] - coords["end_lng"]
    coords["a2"] = np.sin(coords["dlat2"] / 2) ** 2 + np.cos(coords["start_lat"]) * np.cos(coords["end_lat"]) * np.sin(
        coords["dlng2"] / 2) ** 2
    coords["c2"] = 2 * np.arcsin(np.sqrt(coords["a2"]))
    coords["distance2"] = coords["c2"] * 6371

    coords["distance"] = coords["distance1"] + coords["distance2"]
    coords["distance"] *= 1000
    coords["distance"] = coords["distance"].transform(round)

    return coords["distance"]


def fact_dist(ride_df):
    ride_df = ride_df.set_index("rideable_type")
    try:
        ride_df.loc["docked_bike"] *= 317
    except KeyError:
        pass
    try:
        ride_df.loc["classic_bike"] *= 250
    except KeyError:
        pass
    try:
        ride_df.loc["electric_bike"] *= 450
    except KeyError:
        pass
    return ride_df.reset_index()["duration"].transform(int)


for year in range(2013, 2025):
    df = pd.read_csv(f"datasets/tripdata-{year}.csv")

    df["stations_dist"] = stations_dist(df[["start_lat", "start_lng", "end_lat", "end_lng"]])
    df["fact_dist"] = fact_dist(df[["rideable_type", "duration"]])

    df.reset_index().set_index("ride_id").drop('index', axis=1).to_csv(f"mdatasets/tripdata-{year}.csv")
