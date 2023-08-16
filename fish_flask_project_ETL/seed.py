import pandas as pd

sizes_df=pd.read_json("https://data.ny.gov/resource/e52k-ymww.json")
sizes_df.to_csv("ny_fish_sizes.csv", index=False)

water_quality_df=pd.read_json("https://data.ny.gov/resource/8xz8-5u5u.json")
water_quality_df.to_csv("ny_water_qualities.csv", index=False)