import pandas as pd

from api.adapters.client_fish import ClientFish
from api.adapters.client_waterquality import ClientWaterQuality
from api.adapters.fish_adapter import FishAdapter
from api.adapters.waterquality_adapter import WaterQualityAdapter
from api.lib.db import conn, cursor
import awswrangler as wr


# def run_fish(conn, cursor):
#     client_fish=ClientFish()
#     fish_responses = client_fish.request_fishes()
#
#     fishes=[]
#     for response_fish in fish_responses:
#         fish_adapater=FishAdapter(response_fish)
#         fish=fish_adapater.run(conn, cursor)
#         fishes.append(fish)
#
#     return fishes
#
#
# def run_water_quality(conn, cursor):
#     client_waterquality=ClientWaterQuality()
#     waterquality_responses=client_waterquality.request_water_qualities()
#
#     water_qualities=[]
#     for response_water_quality in waterquality_responses:
#         water_quality_adapter=WaterQualityAdapter(response_water_quality)
#         water_quality=water_quality_adapter.run(conn, cursor)
#         water_qualities.append(water_quality)
#
#     return water_qualities
#
# run_fish(conn, cursor)
# run_water_quality(conn, cursor)



def get_fish():
    client_fish=ClientFish()
    fish_responses=client_fish.request_fishes()
    return fish_responses

def save_fish_to_s3(fish_responses, bucket_name):
    fishes_df=pd.DataFrame(fish_responses)

    fishes_parquet_url = f"s3://{bucket_name}/fishes/fishes.snappy.parquet"
    wr.s3.to_parquet(df=fishes_df, path=fishes_parquet_url)

bucket_name="fish-project"
fish_responses=get_fish()
save_fish_to_s3(fish_responses, bucket_name)


def get_water_quality():
    client_water_quality=ClientWaterQuality()
    water_quality_responses=client_water_quality.request_water_qualities()
    return water_quality_responses

def save_water_quality_to_s3(waterquality_responses, bucket_name):
    waterquality_df=pd.DataFrame(waterquality_responses)

    waterqualities_parquet_url = f"s3://{bucket_name}/waterqualities/waterqualities.snappy.parquet"
    wr.s3.to_parquet(df=waterquality_df, path=waterqualities_parquet_url)

bucket_name="fish-project"
fish_responses=get_water_quality()
save_water_quality_to_s3(fish_responses, bucket_name)
