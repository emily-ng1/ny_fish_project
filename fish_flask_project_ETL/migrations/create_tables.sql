DROP TABLE IF EXISTS ny_fishes;
DROP TABLE IF EXISTS ny_water_qualities;


CREATE TABLE IF NOT EXISTS ny_fishes(
    id serial PRIMARY KEY,
    waterbody VARCHAR(255),
    species VARCHAR(255) NOT NULL,
    size_inches DECIMAL,
    number INTEGER,
    month VARCHAR(255),
    year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS fish_species_index ON ny_fishes (species);


CREATE TABLE IF NOT EXISTS ny_water_qualities(
    id serial PRIMARY KEY,
    name VARCHAR(255),
    basin VARCHAR(255),
    description VARCHAR(255),
    water_quality_class VARCHAR(255) NOT NULL,
    waterbody_class VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

