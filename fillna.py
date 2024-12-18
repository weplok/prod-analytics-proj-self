import pandas as pd
import numpy as np

# Тут надо придумать, как заполнить пустые start и end станции

df = pd.read_csv("mdatasets/tripdata-2019.csv")
print("КОЛ-ВО ПРОПУСКОВ В НАЧАЛЕ", len(df[df["start_lat"].isna()]) + len(df[df["end_lat"].isna()]))
stations = df[~df["start_lat"].isna()][["start_station_id", "start_station_name", "start_lat", "start_lng"]]
stations = stations.drop_duplicates(subset=["start_station_id"]).set_index("start_station_id")
mdf = df.merge(stations, on="start_station_id", how="left", suffixes=("", "_new"))
df["start_lat"] = df["start_lat"].fillna(mdf["start_lat_new"])
print(mdf[mdf["start_lat_new"].isna()])
print("КОЛ-ВО ПРОПУСКОВ В КОНЦЕ", len(df[df["start_lat"].isna()]) + len(df[df["end_lat"].isna()]))


'''
df = pd.read_csv("datasets/tripdata-2023.csv")
df["start_lat"] = df["start_lat"].transform(lambda x: str(x))
df["start_lng"] = df["start_lng"].transform(lambda x: str(x))
df["end_lat"] = df["end_lat"].transform(lambda x: str(x))
df["end_lng"] = df["end_lng"].transform(lambda x: str(x))

stations = df[~df["start_station_name"].isna()][["start_station_id", "start_station_name", "start_lat", "start_lng"]]
stations = stations.drop_duplicates(subset=["start_station_id"]).reset_index().set_index("start_station_id").drop("index", axis=1)
stations["start_lat"] = stations["start_lat"].transform(lambda x: str(round(float(x), 2)))
stations["start_lng"] = stations["start_lng"].transform(lambda x: str(round(float(x), 2)))

df = df.head(100)

mdf = df.merge(stations, on=["start_lat", "start_lng"], how="left", suffixes=("", "_new"))
print(mdf)
df["start_station_id"] = df["start_station_id"].fillna(mdf["start_station_id_new"])
print(df)
print("AAAAAAAAAAAAAAAAAAAAa")
df[df["start_station_name"].isna()] = pd.merge(df[df["start_station_name"].isna()], stations, how="left", on=["start_lat", "start_lng"])
stations.rename(columns={
    "start_station_id": "end_station_id",
    "start_station_name": "end_station_name",
    "start_lat": "end_lat",
    "start_lng": "end_lng",
}, inplace=True)
print(df[df["end_station_name"].isna()])
df[df["end_station_name"].isna()] = pd.merge(df[df["end_station_name"].isna()], stations, how="left", on=["end_lat", "end_lng"])
df.dropna().set_index("ride_id")
print(df)
print(df[["start_station_id", "start_lat", "start_lng", "end_station_id", "end_lat", "end_lng"]])
#df.to_csv("tripdata-2020.csv")


df = pd.read_csv("datasets/tripdata-2021.csv")
stations = df[~df["start_station_name"].isna()][["start_station_id", "start_station_name", "start_lat", "start_lng"]]
stations = stations.drop_duplicates(subset=["start_station_id"]).reset_index().set_index("start_station_id").drop("index", axis=1)
stations["start_lat"] = stations["start_lat"].transform(lambda x: round(x, 2))
stations["start_lng"] = stations["start_lng"].transform(lambda x: round(x, 2))
print(stations)
df[df["start_station_name"].isna()] = pd.merge(df[df["start_station_name"].isna()], stations, how="left", on=["start_lat", "start_lng"])
stations.rename(columns={
    "start_station_id": "end_station_id",
    "start_station_name": "end_station_name",
    "start_lat": "end_lat",
    "start_lng": "end_lng",
}, inplace=True)
df[df["end_station_name"].isna()] = pd.merge(df[df["end_station_name"].isna()], stations, how="left", on=["end_lat", "end_lng"])
df.dropna().set_index("ride_id").to_csv("datasets/tripdata-2021.csv")


df = pd.read_csv("datasets/tripdata-2022.csv")
stations = df[~df["start_station_name"].isna()][["start_station_id", "start_station_name", "start_lat", "start_lng"]]
stations = stations.drop_duplicates(subset=["start_station_id"]).reset_index().set_index("start_station_id").drop("index", axis=1)
stations["start_lat"] = stations["start_lat"].transform(lambda x: round(x, 2))
stations["start_lng"] = stations["start_lng"].transform(lambda x: round(x, 2))
stations.to_csv("stations.csv")
df[df["start_station_name"].isna()] = pd.merge(df[df["start_station_name"].isna()], stations, how="left", on=["start_lat", "start_lng"])
stations.rename(columns={
    "start_station_id": "end_station_id",
    "start_station_name": "end_station_name",
    "start_lat": "end_lat",
    "start_lng": "end_lng",
}, inplace=True)
df[df["end_station_name"].isna()] = pd.merge(df[df["end_station_name"].isna()], stations, how="left", on=["end_lat", "end_lng"])
df.set_index("ride_id").to_csv("tripdata-2022.csv")
'''