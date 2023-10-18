from manage import get_fish, save_fish_to_s3, get_water_quality, save_water_quality_to_s3, run_dbt
from settings import bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY
from prefect import task, flow
from data.get_transformed_data_from_s3 import save_csv_from_s3_to_csv


@task
def get_fish_task():
    return get_fish()

@task
def save_fish_to_s3_task(fish_responses, bukcket_name):
    return save_fish_to_s3(fish_responses, bukcket_name)

@task
def get_water_quality_task():
    return get_water_quality()

@task
def save_water_quality_to_s3_task(waterquality_responses, bukcket_name):
    return save_water_quality_to_s3(waterquality_responses, bukcket_name)


@task
def run_dbt_task(dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY):
    return run_dbt(dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY)


@task
def save_files_task(name):
    return save_csv_from_s3_to_csv(name)


@flow
def fish_waterquality_elt(bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY):
    fish_responses=get_fish_task()
    save_fish_to_s3_task(fish_responses, bucket_name)

    waterquality_responses=get_water_quality_task()
    save_water_quality_to_s3_task(waterquality_responses, bucket_name)

    run_dbt_task(dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY)

    save_files_task("dates")
    save_files_task("fishes")
    save_files_task("locations")
    save_files_task("waterbodies")


if __name__=="__main__":
    fish_waterquality_elt(bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY)

#prefect deployment build ./flow.py:fish_waterquality_elt -n get-fishes -q fish-queue -p s3_work_pool
#prefect deployment apply fish_waterquality_elt-deployment.yaml
