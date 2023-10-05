from prefect import task, flow
from manage import *
from api.models.date_model import DateModel
from api.models.water_body_model import WaterbodyModel
from api.models.fish_model import FishModel
from api.models.ny_fish import Fish
from api.models.ny_water_quality import WaterQuality
from api.lib.db import conn, cursor, save_model_dates, save_model_waterbodies, save_model_fishes
from prefect.server.schemas.schedules import IntervalSchedule


#Fish
@task
def get_fish_task():
    return get_fish()

@task
def extract_and_save_fish_infos_task(fish_responses):
    return extract_and_save_fish_infos(fish_responses)

#Waterquality
@task
def get_water_quality_task():
    return get_water_quality()

@task
def extract_and_save_water_quality_infos_task(waterquality_responses):
    return extract_and_save_water_quality_infos(waterquality_responses)


@task
def save_models(conn, Fish, FishModel, DateModel, WaterbodyModel):
    save_model_dates(conn, DateModel, Fish)
    save_model_waterbodies(conn, WaterbodyModel, Fish)
    save_model_fishes(conn, FishModel, DateModel, WaterbodyModel)


@flow
def fish_waterquality_etl():
    fish_responses=get_fish_task()
    #extract_and_save_fish_infos_task(fish_responses)

    waterquality_responses=get_water_quality_task()
    #extract_and_save_water_quality_infos_task(waterquality_responses)

    #save_models(conn, Fish, FishModel, DateModel, WaterbodyModel)

if __name__=="__main__":
    fish_waterquality_etl()

# if __name__=="__main__":
#     fish_waterquality_etl.serve(
#         name="get-fish",
#         schedule=IntervalSchedule(interval=100))

