import pandas as pd
from datetime import date


for year in range(2013, 2025):
    df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
    start_ts = df["started_at"]
    df["start_date"] = start_ts.transform(lambda x: date.fromtimestamp(x).isoformat())
    df = df[["ride_id", "rideable_type", "start_date", "started_at", "ended_at", "start_station_name", "start_station_id",
             "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat", "end_lng", "member_casual",
             "gender", "birthyear", "duration", "cost", "stations_dist","fact_dist"]].set_index("ride_id")
    df.to_csv(f"mdatasets/tripdata-{year}.csv")
    del df
