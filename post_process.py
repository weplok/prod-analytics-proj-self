import pandas as pd
from datetime import datetime as dt
from datetime import date
from add_distance import stations_dist, fact_dist
from costs import *


i = -1
def mapper(x):
    global i
    i += 1
    return i


for year in range(2013, 2025):
    df = pd.read_csv(f"datasets/tripdata-{year}.csv")

    # ВСЕ ДАТЫ - в Таймстамп
    if year == 2013 or year >= 2018:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.fromisoformat(x).timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.fromisoformat(x).timestamp()))
    elif 2014 <= year <= 2015:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()))
    elif 2016 <= year <= 2017:
        df["started_at"] = df["started_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()) if len(x) <= 16 else int(dt.strptime(x, "%m/%d/%Y %H:%M:%S").timestamp()))
        df["ended_at"] = df["ended_at"].transform(lambda x: int(dt.strptime(x, "%m/%d/%Y %H:%M").timestamp()) if len(x) <= 16 else int(dt.strptime(x, "%m/%d/%Y %H:%M:%S").timestamp()))

    # ЗАПОЛНЯЕМ rideable_type, где его нет
    if 2013 <= year <= 2019:
        df["rideable_type"] = "docked_bike"
        col = df.columns.tolist()
        col.remove("rideable_type")
        col.insert(1, "rideable_type")
        df = df[col]

    # ДОБАВЛЯЕМ дату начала поездки
    start_ts = df["started_at"]
    df["start_date"] = start_ts.transform(lambda x: date.fromtimestamp(x).isoformat())
    df_col = df.columns.tolist()
    df_col.remove("start_date")
    df_col.insert(2, "start_date")
    df = df[df_col]

    # ДОБАВЛЯЕМ соцдем, где его нет
    if 2020 <= year <= 2024:
        df["gender"] = np.nan
        df["birthyear"] = np.nan

    # ДОБАВЛЯЕМ длительность поездки
    df["duration"] = round((df["ended_at"] - df["started_at"]) / 60, 2)

    # ДОБАВЛЯЕМ стоимости поездок
    if year in range(2013, 2020):
        df_copy = df.copy()
        df_copy = df_copy.apply(lambda row: [row["member_casual"]] + [row["duration"]], axis=1)
    else:
        df_copy = df.copy()
        df_copy = df_copy.apply(lambda row: [row["member_casual"]] + [row["duration"]] + [row["rideable_type"]], axis=1)
    if year == 2013:
        df["cost"] = df_copy.map(add_cost_2013)
    if year == 2014:
        df["cost"] = df_copy.map(add_cost_2014)
    if year == 2015:
        df["cost"] = df_copy.map(add_cost_2015)
    if year == 2016:
        df["cost"] = df_copy.map(add_cost_2016)
    if year == 2017:
        df["cost"] = df_copy.map(add_cost_2017)
    if year == 2018:
        df["cost"] = df_copy.map(add_cost_2018)
    if year == 2019:
        df["cost"] = df_copy.map(add_cost_2019)
    if year == 2020:
        df["cost"] = df_copy.map(add_cost_2020)
    if year == 2021:
        df["cost"] = df_copy.map(add_cost_2021)
    if year == 2022:
        df["cost"] = df_copy.map(add_cost_2022)
    if year == 2023:
        df["cost"] = df_copy.map(add_cost_2023)
    if year == 2024:
        df["cost"] = df_copy.map(add_cost_2024)

    # ДОБАВЛЯЕМ дистанции - между станциями и фактические
    df["stations_dist"] = stations_dist(df[["start_lat", "start_lng", "end_lat", "end_lng"]])
    df["fact_dist"] = fact_dist(df[["rideable_type", "duration"]])
    df = df.sort_values(by="started_at")

    # УДАЛЯЕМ выбросы
    # поездки < 1 минуты
    df = df[df.duration >= 1]
    # поездки с ролью подчинённого
    if year in range(2015, 2018):
        df = df[df.member_casual != "Dependent"]
    # поездки со слишком большой дистанцией (это тестовые поездки либо выбросы)
    if year in range(2021, 2025):
        df = df[df.stations_dist < 100000]
    # поездки длиннее 30 дней
    if year in range(2018, 2024):
        df = df[df.duration <= 43200]

    # УНИФИЦИРУЕМ ride_id
    s = df["ride_id"]
    s = s.map(mapper)
    df["ride_id"] = s

    df.reset_index().set_index("ride_id").drop('index', axis=1).to_csv(f"mdatasets/tripdata-{year}.csv")
    del df
