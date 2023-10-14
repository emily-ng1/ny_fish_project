{{ config(materialized='external', location='s3://fish-project/mart/locations_mart/locations.csv') }}


WITH stg_fish AS(
    SELECT *
    FROM {{source('s3', 'stg_fish')}}
),

locations AS(
    SELECT county, town
    FROM stg_fish
    GROUP BY county, town
    ORDER BY county, town
),

add_index AS(
    SELECT
    ROW_NUMBER() OVER() AS id,
    county, town,
    CURRENT_TIMESTAMP AS created_at
    FROM locations
)

SELECT * FROM add_index

