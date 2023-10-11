from api.adapters.client_fish import ClientFish
from api.adapters.client_waterquality import ClientWaterQuality
from api.adapters.fish_adapter import FishAdapter
from api.adapters.waterquality_adapter import WaterQualityAdapter
from api.models.date_model import DateModel
from api.models.water_body_model import WaterbodyModel
from api.models.fish_model import FishModel
from api.models.ny_fish import Fish
from api.models.ny_water_quality import WaterQuality
from api.lib.db import conn, cursor, save_model_dates, save_model_waterbodies, save_model_fishes
from api.lib.db import save

#conn and cursor object

def get_fish():
    client_fish=ClientFish()
    fish_responses=client_fish.request_fishes()
    return fish_responses

def extract_and_save_fish_infos(fish_responses):
    fishes=[]
    for response_fish in fish_responses:
        fish_adapater=FishAdapter(response_fish)
        fish=fish_adapater.run(conn, cursor)
        fishes.append(fish)

    return fishes


def get_water_quality():
    client_water_quality=ClientWaterQuality()
    water_quality_responses=client_water_quality.request_water_qualities()
    return water_quality_responses

def extract_and_save_water_quality_infos(waterquality_responses):
    water_qualities=[]
    for response_water_quality in waterquality_responses:
        water_quality_adapter=WaterQualityAdapter(response_water_quality)
        water_quality=water_quality_adapter.run(conn, cursor)
        water_qualities.append(water_quality)

    return water_qualities



# def run_fish(conn, cursor):
#     client_fish=ClientFish()
#     fish_responses=client_fish.request_fishes()
#
#     fishes=[]
#     for response_fish in fish_responses:
#         fish_adapater=FishAdapter(response_fish)
#         fish=fish_adapater.run(conn, cursor)
#         fishes.append(fish)
#
#     return fishes


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



