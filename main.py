from matplotlib import pyplot as plt
import pandas as pd


def day_rides_costs():
    df = pd.read_csv("data_marts/rides_per_day.csv")
    x = df["sum_costs"]
    y = df["count_rides"]
    plt.figure(figsize=(15, 10))
    plt.scatter(x, y)
    plt.show()


df = pd.read_csv("datasets/tripdata-full.csv")
dur = df[["started_at", "duration"]]
del df
plt.figure(figsize=(20, 10))
plt.scatter(dur["started_at"], dur["duration"])
plt.show()