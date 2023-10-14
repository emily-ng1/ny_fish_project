{{ config(materialized='external', location='s3://fish-project/staging/fishes_staging/fishes.snappy.parquet') }}


WITH fishes AS(
    SELECT * FROM {{source('s3', 'fish')}}
),

rename_fishes AS(
    SELECT
    month,
    year,
    county,
    town,
    waterbody AS name,
    number,
    species AS species_name,
    size_inches
    FROM fishes
)

SELECT * FROM rename_fishes
