import pandas as pd
import datetime as dt


df = pd.read_csv("2023-divvy-tripdata.csv")
df["duration"] = ((df["ended_at"]
                  .transform(lambda x: dt.datetime.fromisoformat(x).timestamp()) -
                  df["started_at"]
                  .transform(lambda x: dt.datetime.fromisoformat(x).timestamp()))
                  / 60 + 1
                  ).transform(lambda x: int(x))

print(df)