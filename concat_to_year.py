import pandas as pd

df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])

for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    df_month = pd.read_csv(f"raw_data/2023{month}-divvy-tripdata.csv")
    df = pd.concat([df, df_month])

df = df.reset_index().set_index("ride_id").drop('index', axis=1)



df.to_csv("2023-divvy-tripdata.csv")