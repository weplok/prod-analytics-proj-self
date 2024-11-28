import pandas as pd


df = pd.DataFrame(columns=["id", "name", "latitude", "longitude", "dpcapacity", "online_date"])

df_2013 = pd.read_csv("raw_data/Divvy_Stations_2013.csv")
df_2013.drop("landmark", axis=1)
df = pd.concat([df, df_2013])
