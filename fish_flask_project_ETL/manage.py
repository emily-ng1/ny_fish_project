from api.adapters.client_fish import ClientFish
from api.adapters.client_waterquality import ClientWaterQuality
from api.adapters.fish_adapter import FishAdapter
from api.adapters.waterquality_adapter import WaterQualityAdapter
from api.lib.db import conn, cursor


def run_fish(conn, cursor):
    client_fish=ClientFish()
    fish_responses = client_fish.request_fishes()

    fishes=[]
    for response_fish in fish_responses:
        fish_adapater=FishAdapter(response_fish)
        fish=fish_adapater.run(conn, cursor)
        fishes.append(fish)

    return fishes


def run_water_quality(conn, cursor):
    client_waterquality=ClientWaterQuality()
    waterquality_responses=client_waterquality.request_water_qualities()

    water_qualities=[]
    for response_water_quality in waterquality_responses:
        water_quality_adapter=WaterQualityAdapter(response_water_quality)
        water_quality=water_quality_adapter.run(conn, cursor)
        water_qualities.append(water_quality)

    return water_qualities

run_fish(conn, cursor)
run_water_quality(conn, cursor)