DROP TABLE IF EXISTS ny_fishes;
DROP TABLE IF EXISTS ny_water_qualities;


CREATE TABLE IF NOT EXISTS ny_fishes(
    id serial PRIMARY KEY,
    year INTEGER,
    county VARCHAR(255),
    waterbody VARCHAR(255),
    town VARCHAR(255),
    month VARCHAR(255),
    number INTEGER,
    species VARCHAR(255) NOT NULL,
    size_inches DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS fish_species_index ON ny_fishes (species);


CREATE TABLE IF NOT EXISTS ny_water_qualities(
    id serial PRIMARY KEY,
    waterbody_class VARCHAR(255),
    segment_id VARCHAR(255),
    win VARCHAR(255),
    name VARCHAR(255),
    description VARCHAR(255),
    basin VARCHAR(255),
    part INTEGER,
    water_quality_class VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--\copy ny_fishes (year, county, waterbody, town, month, number, species, size_inches) FROM 'data/ny_fish_sizes.csv' DELIMITER ',' CSV HEADER;
--\copy ny_water_qualities (waterbody_class, segment_id, win, name,description, basin, part, water_quality_class) from 'data/ny_water_qualities.csv' DELIMITER ',' CSV HEADER;