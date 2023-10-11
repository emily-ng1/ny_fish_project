from manage import get_fish, save_fish_to_s3, get_water_quality, save_water_quality_to_s3
from settings import bucket_name
from prefect import task, flow


@task
def get_fish_task():
    get_fish()

@task
def save_fish_to_s3_task(fish_responses, bukcket_name):
    save_fish_to_s3(fish_responses, bukcket_name)

@task
def get_water_quality_task():
    get_water_quality()

@task
def save_water_quality_to_s3_task(waterquality_responses, bukcket_name):
    save_water_quality_to_s3(waterquality_responses, bukcket_name)


@flow
def fish_waterquality_etl(bucket_name):
    fish_responses=get_fish_task()
    save_fish_to_s3_task(fish_responses, bucket_name)

    waterquality_responses=get_water_quality_task()
    save_water_quality_to_s3_task(waterquality_responses, bucket_name)

if __name__=="__main__":
    fish_waterquality_etl(bucket_name)
