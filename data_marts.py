import pandas as pd
from datetime import date


def stations_fact_dist(output_mart):
    data = list()
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        sum_st_dist = df["stations_dist"].sum() // 1000
        sum_fact_dist = df["fact_dist"].sum() // 1000
        data.append([year, sum_st_dist, sum_fact_dist])
        del df
    ans = pd.DataFrame(columns=["year", "sum_stations_dist", "sum_fact_dist"], data=data)
    ans.reset_index().set_index("year").drop('index', axis=1).to_csv(output_mart)


def ride_count(output_mart):
    data = list()
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        member_ride_c = len(df[df.member_casual == "member"])
        casual_ride_c = len(df[df.member_casual == "casual"])

        walks = df[df.stations_dist == 0.0]
        member_walk_c = len(walks[walks.member_casual == "member"])
        casual_walk_c = len(walks[walks.member_casual == "casual"])

        procent_m_walks = round((member_walk_c / member_ride_c) * 100, 2)
        procent_c_walks = round((casual_walk_c / casual_ride_c) * 100, 2)

        data.append(
            [year, member_ride_c, member_walk_c, procent_m_walks, casual_ride_c, casual_walk_c, procent_c_walks])
        del df
    ans = pd.DataFrame(
        columns=["year", "member_ride_count", "member_walk_count","%_member_walks",
                 "casual_ride_count", "casual_walk_count", "%_casual_walks"],
        data=data,
    )
    ans.reset_index().set_index("year").drop('index', axis=1).to_csv(output_mart)


def member_casual_costs(output_mart):
    data = list()
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        for rt in ["docked_bike", "classic_bike", "electric_bike"]:
            rt_df = df[df.rideable_type == rt]
            member_cost = round(rt_df[rt_df.member_casual == "member"]["cost"].sum())
            casual_cost = round(rt_df[rt_df.member_casual == "casual"]["cost"].sum())
            data.append([year, rt, member_cost, casual_cost])
        del df
    ans = pd.DataFrame(columns=["year", "rt", "member_cost", "casual_cost"], data=data)
    ans.reset_index().set_index("year").drop('index', axis=1).to_csv(output_mart)


def rides_per_day(output_mart):
    ans = pd.DataFrame(columns=["ride_id", "cost"])
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        agg = df.groupby("start_date").agg({"ride_id": "count", "cost": "sum"})
        ans = pd.concat([ans, agg])
        del df
    ans = ans.reset_index()
    ans.rename(columns={"index": "start_date", "ride_id": "count_rides", "cost": "sum_costs"}, inplace=True)
    ans = ans.dropna(axis=0)
    ans.to_csv(output_mart)


def day_rides_costs():
    df = pd.read_csv("data_marts/rides_per_day.csv")
    x = df["sum_costs"]
    y = df["count_rides"]
    plt.figure(figsize=(15, 10))
    plt.scatter(x, y)
    plt.show()

def durations():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    dur = df[["ride_id", "start_date", "duration", "cost"]]
    del df
    dur_bad = dur[dur.duration < 1][dur.duration >= 0]
    dur_bad.to_csv("data_marts/dur_so_so.csv")


def str_values():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    gender = df.groupby("gender").agg({"gender": "count"})
    mc = df.groupby("member_casual").agg({"member_casual": "count"})
    by = df.groupby("birthyear").agg({"birthyear": "count"})
    print(gender)
    print(mc)
    by.to_csv("data_marts/birthyear.csv")


def big_dist():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    df_big = df[df.stations_dist > 100000]
    del df
    df_big.to_csv("data_marts/big_dist.csv")


def long_rides():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    df_long = df[df.duration > 43200]
    del df
    df_long.to_csv("data_marts/long_rides.csv")

def unreal_socdem():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    df_uoy = df[df.birthyear >= 2013]
    df_uyy = df[df.birthyear <= 1918]
    del df
    df_uy = pd.concat([df_uoy, df_uyy]).sort_values(by="start_date")
    df_uy.to_csv("data_marts/unreal_birthyear.csv")



if __name__ == "__main__":
    stations_fact_dist("data_marts/stations_fact_dist.csv")
    #ride_count("data_marts/member_casual_rides.csv")
    member_casual_costs("data_marts/member_casual_cost.csv")
    rides_per_day("data_marts/rides_per_day.csv")
