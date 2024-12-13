import pandas as pd
from sklearn.linear_model import LinearRegression


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
        columns=["year", "member_ride_count", "member_walk_count", "%_member_walks",
                 "casual_ride_count", "casual_walk_count", "%_casual_walks"],
        data=data,
    )
    ans.reset_index().set_index("year").drop('index', axis=1).to_csv(output_mart)


def member_casual_costs(output_mart):
    data = list()
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            for MC in ["member", "casual"]:
                df_month = df[df["start_date"].str.contains(f"{year}-{month}")]
                df_month_MC = df_month[df_month.member_casual == MC].agg({
                    "ride_id": "count",
                    "cost": "sum",
                })
                data.append(
                    [
                        year,
                        month,
                        MC,
                        int(df_month_MC["ride_id"]),
                        round(df_month_MC["cost"], 2),
                        round(df_month_MC["cost"] / df_month_MC["ride_id"], 2)
                    ])
        del df
    ans = pd.DataFrame(columns=["year", "month", "member_casual", "count_rides", "sum_costs", "avg_check"], data=data)
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


def str_values():
    df = pd.read_csv("mdatasets/tripdata-full.csv")
    gender = df.groupby("gender").agg({"gender": "count"})
    mc = df.groupby("member_casual").agg({"member_casual": "count"})
    by = df.groupby("birthyear").agg({"birthyear": "count"})
    print(gender)
    print(mc)
    by.to_csv("data_marts/birthyear.csv")


def socdem_mart():
    data = []

    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
        df_males = df[df.gender == "Male"]
        df_females = df[df.gender == "Female"]

        year_data = {
            "year": year,
            "males_count": df_males["ride_id"].count(),
            "females_count": df_females["ride_id"].count(),
            "males_avg_by": round(df_males["birthyear"].mean(), 2),
            "females_avg_by": round(df_females["birthyear"].mean(), 2),
            "total_avg_by": round(df["birthyear"].mean(), 2),
        }
        data.append(year_data)

    sd_df = pd.DataFrame(
        columns=["year", "males_count", "females_count", "males_avg_by", "females_avg_by", "total_avg_by"],
        data=data,
    ).set_index("year")
    sd_df.to_csv("data_marts/socdem_mart.csv")


def bikes_stations_count():
    data = []
    for year in range(2013, 2025):
        df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")

        year_data = {
            "year": year,
            "bikes_count": len(df["bike_id"].unique()),
            "stations_count": len(pd.concat([df["start_station_id"], df["end_station_id"]]).unique()),
        }
        if year == 2020:
            year_data["stations_count"] = len(pd.concat([df["start_station_name"], df["end_station_name"]]).unique())
        data.append(year_data)

    bs_df = pd.DataFrame(
        columns=["year", "bikes_count", "stations_count"],
        data=data,
    ).set_index("year")

    df_train = bs_df[bs_df.bikes_count != 1]
    x_train = df_train[["stations_count"]]
    y_train = df_train["bikes_count"]

    model = LinearRegression()
    model.fit(x_train, y_train)

    test_df = bs_df[bs_df.bikes_count == 1]
    x_test = test_df[["stations_count"]]
    predictions = model.predict(x_test)

    bs_df.loc[bs_df.bikes_count == 1, "bikes_count"] = predictions
    bs_df["bikes_count"] = bs_df["bikes_count"].transform(lambda x: int(x))
    bs_df.to_csv("data_marts/bikes_stations_count.csv")


if __name__ == "__main__":
    member_casual_costs("data_marts/costs_per_month.csv")
