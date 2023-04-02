import pandas as pd

sizes_df=pd.read_json("https://data.ny.gov/resource/e52k-ymww.json")
sizes_df.to_csv("ny_fish_sizes.csv", index=False)
