{{ config(materialized='external', location='s3://fish-project/staging/waterqualities_staging/waterqualities.snappy.parquet') }}


WITH waterqualities AS(
    SELECT * FROM {{source('s3', 'waterquality')}}
),

rename_waterqualities AS(
    SELECT
    waterbody_class AS waterbody_type,
    name,
    description,
    basin AS basin_name,
    water_quality_class
    FROM waterqualities
)

SELECT * FROM rename_waterqualities