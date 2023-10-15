import pandas as pd
import awswrangler as wr
from api.adapters.client_fish import ClientFish
from api.adapters.client_waterquality import ClientWaterQuality

import subprocess
import os


def get_fish():
    client_fish=ClientFish()
    fish_responses=client_fish.request_fishes()
    return fish_responses

def save_fish_to_s3(fish_responses, bucket_name):
    fishes_df=pd.DataFrame(fish_responses)
    fishes_parquet_url = f"s3://{bucket_name}/source/fishes/fishes.snappy.parquet"
    wr.s3.to_parquet(df=fishes_df, path=fishes_parquet_url)

    print(wr.s3.read_parquet(path=f"s3://{bucket_name}/source/fishes/fishes.snappy.parquet")[0:3])

# bucket_name="fish-project"
# fish_responses=get_fish()
# save_fish_to_s3(fish_responses, bucket_name)
# print(wr.s3.read_parquet(path=f"s3://{bucket_name}/source/fishes/fishes.snappy.parquet"))


def get_water_quality():
    client_water_quality=ClientWaterQuality()
    water_quality_responses=client_water_quality.request_water_qualities()
    return water_quality_responses

def save_water_quality_to_s3(waterquality_responses, bucket_name):
    waterquality_df=pd.DataFrame(waterquality_responses)
    waterqualities_parquet_url = f"s3://{bucket_name}/source/waterqualities/waterqualities.snappy.parquet"
    wr.s3.to_parquet(df=waterquality_df, path=waterqualities_parquet_url)

    print(wr.s3.read_parquet(path=f"s3://{bucket_name}/source/waterqualities/waterqualities.snappy.parquet")[0:3])

# bucket_name="fish-project"
# waterquality_responses=get_water_quality()
# save_water_quality_to_s3(waterquality_responses, bucket_name)
# print(wr.s3.read_parquet(path=f"s3://{bucket_name}/source/waterqualities/waterqualities.snappy.parquet"))

# print(wr.s3.read_parquet(path=f"s3://fish-project/mart/dates_mart/dates.snappy.parquet"))
# print(wr.s3.read_parquet(path=f"s3://fish-project/mart/waterbodies_mart/waterbodies.snappy.parquet"))
# print(wr.s3.read_parquet(path=f"s3://fish-project/mart/locations_mart/locations.snappy.parquet"))

# print(wr.s3.read_parquet(path=f"s3://fish-project/mart/fishes_mart/fishes.snappy.parquet"))


def run_dbt(dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY):
    try:
        os.environ['S3_ACCESS_KEY_ID'] = S3_ACCESS_KEY_ID
        os.environ['S3_SECRET_ACCESS_KEY'] = S3_SECRET_ACCESS_KEY

        os.chdir(dbt_file_path) #dbt filepath

        subprocess.run(["dbt", "run"], check=True) #dbt run command
        print("dbt run successful.")
    except subprocess.CalledProcessError as e:
        print(f"dbt run failed with error: {e}")
    finally:
        os.chdir(os.path.dirname(os.path.realpath(__file__))) #Change back to the original directory

