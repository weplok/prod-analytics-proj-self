import pandas as pd

'''
df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]:
    df_month = pd.read_csv(f"raw_data/2024{month}-divvy-tripdata.csv")
    df = pd.concat([df, df_month])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2024.csv")'''

'''
df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    df_month = pd.read_csv(f"raw_data/2023{month}-divvy-tripdata.csv")
    df = pd.concat([df, df_month])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2023.csv")'''

'''
df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    if month != "09":
        df_month = pd.read_csv(f"raw_data/2022{month}-divvy-tripdata.csv")
    else:
        df_month = pd.read_csv("raw_data/202209-divvy-publictripdata.csv")
    df = pd.concat([df, df_month])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2022.csv")'''

'''
df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    df_month = pd.read_csv(f"raw_data/2021{month}-divvy-tripdata.csv")
    df = pd.concat([df, df_month])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2021.csv")'''

'''
df = pd.DataFrame(columns=["ride_id" ,"rideable_type", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_quart = pd.read_csv("raw_data/Divvy_Trips_2020_Q1.csv")
df = pd.concat([df, df_quart])
for month in ["04", "05", "06", "07", "08", "09", "10", "11", "12"]:
    df_month = pd.read_csv(f"raw_data/2020{month}-divvy-tripdata.csv")
    df = pd.concat([df, df_month])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2020.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2013.csv")
df_stations = pd.read_csv("raw_data/Divvy_Stations_2013.csv")[["id", "latitude", "longitude"]]
df_quart.rename(columns={
    "trip_id": "ride_id",
    "starttime": "started_at",
    "stoptime": "ended_at",
    "from_station_id": "start_station_id",
    "from_station_name": "start_station_name",
    "to_station_id": "end_station_id",
    "to_station_name": "end_station_name",
    "usertype": "member_casual",
}, inplace=True)
df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
df_quart.rename(columns={
    "latitude": "start_lat",
    "longitude": "start_lng",
    "id": "id_x",
}, inplace=True)
df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
df_quart.rename(columns={
    "latitude": "end_lat",
    "longitude": "end_lng",
    "id": "id_y",
}, inplace=True)
df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                    "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                    "end_lng", "member_casual", "gender", "birthyear"]]

df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2013.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations1 = pd.read_csv("raw_data/Divvy_Stations_2014-Q1Q2.csv")[["id", "latitude", "longitude"]]
df_stations2 = pd.read_csv("raw_data/Divvy_Stations_2014-Q3Q4.csv")[["id", "latitude", "longitude"]]
df_stations = pd.concat([df_stations1, df_stations2])
for quart in ["_Q1Q2", "-Q3-07", "-Q3-0809", "-Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2014{quart}.csv")
    df_quart.rename(columns={
        "trip_id": "ride_id",
        "starttime": "started_at",
        "stoptime": "ended_at",
        "from_station_id": "start_station_id",
        "from_station_name": "start_station_name",
        "to_station_id": "end_station_id",
        "to_station_name": "end_station_name",
        "usertype": "member_casual",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2014.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations = pd.read_csv("raw_data/Divvy_Stations_2015.csv")[["id", "latitude", "longitude"]]
for quart in ["-Q1", "-Q2", "_07", "_08", "_09", "_Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2015{quart}.csv")
    df_quart.rename(columns={
        "trip_id": "ride_id",
        "starttime": "started_at",
        "stoptime": "ended_at",
        "from_station_id": "start_station_id",
        "from_station_name": "start_station_name",
        "to_station_id": "end_station_id",
        "to_station_name": "end_station_name",
        "usertype": "member_casual",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2015.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations1 = pd.read_csv("raw_data/Divvy_Stations_2016_Q1Q2.csv")[["id", "latitude", "longitude"]]
df_stations2 = pd.read_csv("raw_data/Divvy_Stations_2016_Q3.csv")[["id", "latitude", "longitude"]]
df_stations3 = pd.read_csv("raw_data/Divvy_Stations_2016_Q4.csv")[["id", "latitude", "longitude"]]
df_stations = pd.concat([df_stations1, df_stations2, df_stations3])
for quart in ["_Q1", "_04", "_05", "_06", "_Q3", "_Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2016{quart}.csv")
    df_quart.rename(columns={
        "trip_id": "ride_id",
        "starttime": "started_at",
        "stoptime": "ended_at",
        "from_station_id": "start_station_id",
        "from_station_name": "start_station_name",
        "to_station_id": "end_station_id",
        "to_station_name": "end_station_name",
        "usertype": "member_casual",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2016.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations1 = pd.read_csv("raw_data/Divvy_Stations_2017_Q1Q2.csv")[["id", "latitude", "longitude"]]
df_stations2 = pd.read_csv("raw_data/Divvy_Stations_2017_Q3Q4.csv")[["id", "latitude", "longitude"]]
df_stations = pd.concat([df_stations1, df_stations2])
for quart in ["_Q1", "_Q2", "_Q3", "_Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2017{quart}.csv")
    df_quart.rename(columns={
        "trip_id": "ride_id",
        "start_time": "started_at",
        "end_time": "ended_at",
        "from_station_id": "start_station_id",
        "from_station_name": "start_station_name",
        "to_station_id": "end_station_id",
        "to_station_name": "end_station_name",
        "usertype": "member_casual",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2017.csv")'''

'''
df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations1 = pd.read_csv("raw_data/Divvy_Stations_2017_Q1Q2.csv")[["id", "latitude", "longitude"]]
df_stations2 = pd.read_csv("raw_data/Divvy_Stations_2017_Q3Q4.csv")[["id", "latitude", "longitude"]]
df_stations = pd.concat([df_stations1, df_stations2])
for quart in ["_Q1", "_Q2", "_Q3", "_Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2018{quart}.csv")
    if quart != "_Q1":
        df_quart.rename(columns={
            "trip_id": "ride_id",
            "start_time": "started_at",
            "end_time": "ended_at",
            "from_station_id": "start_station_id",
            "from_station_name": "start_station_name",
            "to_station_id": "end_station_id",
            "to_station_name": "end_station_name",
            "usertype": "member_casual",
        }, inplace=True)
    else:
        df_quart.rename(columns={
            "01 - Rental Details Rental ID": "ride_id",
            "01 - Rental Details Local Start Time": "started_at",
            "01 - Rental Details Local End Time": "ended_at",
            "03 - Rental Start Station ID": "start_station_id",
            "03 - Rental Start Station Name": "start_station_name",
            "02 - Rental End Station ID": "end_station_id",
            "02 - Rental End Station Name": "end_station_name",
            "User Type": "member_casual",
            "Member Gender": "gender",
            "05 - Member Details Member Birthday Year": "birthyear",
            "01 - Rental Details Bike ID": "bikeid",
            "01 - Rental Details Duration In Seconds Uncapped": "tripduration",
        }, inplace=True)
        print(df_quart)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2018.csv")'''


df = pd.DataFrame(columns=["ride_id", "started_at", "ended_at", "start_station_name",
                           "start_station_id", "end_station_name", "end_station_id", "start_lat",
                           "start_lng", "end_lat", "end_lng", "member_casual"])
df_stations1 = pd.read_csv("raw_data/Divvy_Stations_2017_Q1Q2.csv")[["id", "latitude", "longitude"]]
df_stations2 = pd.read_csv("raw_data/Divvy_Stations_2017_Q3Q4.csv")[["id", "latitude", "longitude"]]
df_stations = pd.concat([df_stations1, df_stations2])
for quart in ["_Q1", "_Q2", "_Q3", "_Q4"]:
    df_quart = pd.read_csv(f"raw_data/Divvy_Trips_2019{quart}.csv")
    if quart != "_Q2":
        df_quart.rename(columns={
            "trip_id": "ride_id",
            "start_time": "started_at",
            "end_time": "ended_at",
            "from_station_id": "start_station_id",
            "from_station_name": "start_station_name",
            "to_station_id": "end_station_id",
            "to_station_name": "end_station_name",
            "usertype": "member_casual",
        }, inplace=True)
    else:
        df_quart.rename(columns={
            "01 - Rental Details Rental ID": "ride_id",
            "01 - Rental Details Local Start Time": "started_at",
            "01 - Rental Details Local End Time": "ended_at",
            "03 - Rental Start Station ID": "start_station_id",
            "03 - Rental Start Station Name": "start_station_name",
            "02 - Rental End Station ID": "end_station_id",
            "02 - Rental End Station Name": "end_station_name",
            "User Type": "member_casual",
            "Member Gender": "gender",
            "05 - Member Details Member Birthday Year": "birthyear",
            "01 - Rental Details Bike ID": "bikeid",
            "01 - Rental Details Duration In Seconds Uncapped": "tripduration",
        }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="start_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "start_lat",
        "longitude": "start_lng",
        "id": "id_x",
    }, inplace=True)
    df_quart = pd.merge(df_quart, df_stations, left_on="end_station_id", right_on="id", how="left")
    df_quart.rename(columns={
        "latitude": "end_lat",
        "longitude": "end_lng",
        "id": "id_y",
    }, inplace=True)
    df_quart = df_quart.drop(columns=["id_x", "id_y", "bikeid", "tripduration"])
    df_quart.loc[df_quart["member_casual"] == "Customer", "member_casual"] = "casual"
    df_quart.loc[df_quart["member_casual"] == "Subscriber", "member_casual"] = "member"
    df_quart = df_quart[["ride_id", "started_at", "ended_at", "start_station_name", "start_station_id",
                         "end_station_name", "end_station_id", "start_lat", "start_lng", "end_lat",
                         "end_lng", "member_casual", "gender", "birthyear"]]
    df = pd.concat([df, df_quart])
df = df.reset_index().set_index("ride_id").drop('index', axis=1)
df.to_csv("datasets/tripdata-2019.csv")
