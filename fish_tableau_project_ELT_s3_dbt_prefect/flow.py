from manage import get_fish, save_fish_to_s3, get_water_quality, save_water_quality_to_s3, run_dbt
from settings import bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY
from prefect import task, flow


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


@flow
def fish_waterquality_elt(bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY):
    fish_responses=get_fish_task()
    save_fish_to_s3_task(fish_responses, bucket_name)

    waterquality_responses=get_water_quality_task()
    save_water_quality_to_s3_task(waterquality_responses, bucket_name)

    run_dbt_task(dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY)


if __name__=="__main__":
    fish_waterquality_elt(bucket_name, dbt_file_path, S3_ACCESS_KEY_ID, S3_SECRET_ACCESS_KEY)

#prefect deployment build ./flow.py:fish_waterquality_elt -n get-fishes -q fish-queue -p s3_work_pool
#prefect deployment apply fish_waterquality_elt-deployment.yaml
