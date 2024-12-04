import pandas as pd
from datetime import datetime as dt


for year in range(2013, 2025):
    df = pd.read_csv(f"datasets/tripdata-{year}.csv")

    if year == 2013 or year >= 2018:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.fromisoformat(x).timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.fromisoformat(x).timestamp()))
    elif 2014 <= year <= 2015:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()))
    elif 2016 <= year <= 2017:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()) if len(x) <= 16 else int(dt.strptime(x, "%m/%d/%Y %H:%M:%S").timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()) if len(x) <= 16 else int(dt.strptime(x, "%m/%d/%Y %H:%M:%S").timestamp()))

    if 2013 <= year <= 2019:
        df["rideable_type"] = "docked_bike"
        col = df.columns.tolist()
        col.remove("rideable_type")
        col.insert(1, "rideable_type")
        df = df[col]

    df["duration"] = round((df["ended_at"] - df["started_at"]) / 60, 2)
    df = df.sort_values(by="started_at")

    df.reset_index().set_index("ride_id").drop('index', axis=1).to_csv(f"datasets/tripdata-{year}.csv")
    del df
