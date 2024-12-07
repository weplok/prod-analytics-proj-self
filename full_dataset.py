import pandas as pd


main_df = pd.read_csv("mdatasets/tripdata-2013.csv")
for year in range(2014, 2025):
    df = pd.read_csv(f"mdatasets/tripdata-{year}.csv")
    main_df = pd.concat([main_df, df])
    del df
main_df = main_df.reset_index().set_index("ride_id").drop('index', axis=1)
main_df.to_csv("mdatasets/tripdata-full.csv")