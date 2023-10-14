{{ config(materialized='external', location='s3://fish-project/mart/dates_mart/dates.csv') }}


WITH distinct_dates AS(
    SELECT month, year
    FROM {{source('s3', 'stg_fish')}}
    GROUP BY month, year
),

order_by_month AS(
    SELECT
    month, year
    FROM distinct_dates
    ORDER BY
    (CASE
        WHEN month='January' THEN 1
        WHEN month='February' THEN 2
        WHEN month='March' THEN 3
        WHEN month='April' THEN 4
        WHEN month='May' THEN 5
        WHEN month='June' THEN 6
        WHEN month='July' THEN 7
        WHEN month='August' THEN 8
        WHEN month='September' THEN 9
        WHEN month='October' THEN 10
        WHEN month='November' THEN 11
        WHEN month='December' THEN 12
        ELSE 99 END), year
),

add_index AS(
    SELECT
    ROW_NUMBER() OVER() AS id,
    month, year,
    CURRENT_TIMESTAMP AS created_at
    FROM order_by_month
)

SELECT * FROM add_index