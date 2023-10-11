WITH fishes AS(
    SELECT * FROM {{source('s3', 'fish')}}
)

SELECT * FROM fishes


