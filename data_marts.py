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
        df = pd.read_csv(f"datasets/tripdata-{year}.csv")
        for rt in ["docked_bike", "classic_bike", "electric_bike"]:
            rt_df = df[df.rideable_type == rt]
            member_cost = round(rt_df[rt_df.member_casual == "member"]["cost"].sum())
            casual_cost = round(rt_df[rt_df.member_casual == "casual"]["cost"].sum())
            data.append([year, rt, member_cost, casual_cost])
        del df
    ans = pd.DataFrame(columns=["year", "rt", "member_cost", "casual_cost"], data=data)
    ans.reset_index().set_index("year").drop('index', axis=1).to_csv(output_mart)


def rides_per_day(output_mart):
    data = list()
    year_ts = {2013: 1356984000, 2014: 1388520000, 2015: 1420059600, 2016: 1451595600,
               2017: 1483218000, 2018: 1514754000, 2019: 1546290000, 2020: 1577826000,
               2021: 1609448400, 2022: 1640984400, 2023: 1672520400, 2024: 1704056400,
               2025: 1735678800}
    for year in range(2013, 2021):
        df = pd.read_csv(f"datasets/tripdata-{year}.csv")
        for day in range(year_ts[year], year_ts[year + 1], 86400):
            day_df = df[df.started_at >= day][df.started_at < day + 86400]
            data.append([date.fromtimestamp(day), len(day_df), day_df["cost"].sum()])
        del df
    ans = pd.DataFrame(columns=["day", "rides_count", "day_costs"], data=data)
    print(ans)
    ans.set_index("day").to_csv(output_mart)


if __name__ == "__main__":
    #stations_fact_dist("data_marts/stations_fact_dist.csv")
    #ride_count("data_marts/member_casual_rides.csv")
    #member_casual_costs("data_marts/member_casual_cost.csv")
    rides_per_day("data_marts/rides_per_day.csv")
