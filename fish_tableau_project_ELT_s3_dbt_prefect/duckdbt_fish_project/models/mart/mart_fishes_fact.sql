{{ config(materialized='external', location='s3://fish-project/mart/fishes_mart/fishes.csv') }}


WITH stg_fish AS(
    SELECT * FROM {{source('s3', 'stg_fish')}}
),

mart_dates AS(
    SELECT * FROM {{ref('mart_dates_dim')}}
),

mart_waterbodies AS(
    SELECT * FROM {{ref('mart_waterbodies_dim')}}
),

mart_locations AS(
    SELECT * FROM {{ref('mart_locations_dim')}}
),

combine_tables AS(
    SELECT
    c.id AS waterbody_id, b.id AS date_id, d.id AS location_id,
    a.species_name, a.size_inches, a.number
    FROM stg_fish a
    INNER JOIN mart_dates b ON a.month=b.month AND a.year=b.year
    INNER JOIN mart_waterbodies c ON a.name=c.name
    INNER JOIN mart_locations d ON a.county=d.county AND a.town=d.town
    GROUP BY waterbody_id, date_id, location_id, a.species_name, a.size_inches, a.number
    ORDER BY waterbody_id, date_id, location_id, a.species_name, a.size_inches, a.number
),

add_index AS(
    SELECT ROW_NUMBER() OVER() AS id,
    waterbody_id, date_id, location_id, species_name, size_inches, number,
    CURRENT_TIMESTAMP AS created_at
    FROM combine_tables
)

SELECT * FROM add_index