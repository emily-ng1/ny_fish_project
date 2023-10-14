{{ config(materialized='external', location='s3://fish-project/mart/waterbodies_mart/waterbodies.csv') }}


WITH stg_fish AS(
    SELECT *
    FROM {{source('s3', 'stg_fish')}}
),

stg_waterqualities AS(
    SELECT *
    FROM {{source('s3', 'stg_waterquality')}}
),

waterbodies AS(
    SELECT a.name AS name, b.waterbody_type, b.description, b.basin_name, b.water_quality_class
    FROM stg_fish a
    INNER JOIN stg_waterqualities b ON a.name=b.name
    GROUP BY a.name, b.waterbody_type, b.description, b.basin_name, b.water_quality_class
    ORDER BY a.name
),

add_index AS(
    SELECT ROW_NUMBER() OVER() AS id,
    name, waterbody_type, description, basin_name, water_quality_class,
    CURRENT_TIMESTAMP AS created_at
    FROM waterbodies
)

SELECT * FROM add_index