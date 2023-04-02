DROP TABLE IF EXISTS ny_fishes;

CREATE TABLE IF NOT EXISTS ny_fishes(
    id serial PRIMARY KEY,
    year INTEGER,
    county VARCHAR(255),
    waterbody VARCHAR(255),
    town VARCHAR(255),
    month VARCHAR(255),
    number INTEGER,
    species VARCHAR(255),
    size_inches DECIMAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS fish_species_index ON ny_fishes (species);