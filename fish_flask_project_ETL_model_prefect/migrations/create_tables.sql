DROP TABLE IF EXISTS fishes;
DROP TABLE IF EXISTS waterbodies;
DROP TABLE IF EXISTS dates;
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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_ny_fishes UNIQUE (waterbody, species, size_inches, number, month, year)
);

CREATE INDEX IF NOT EXISTS fish_species_index ON ny_fishes (species);


CREATE TABLE IF NOT EXISTS ny_water_qualities(
    id serial PRIMARY KEY,
    name VARCHAR(255),
    basin VARCHAR(255),
    description VARCHAR(255),
    water_quality_class VARCHAR(255) NOT NULL,
    waterbody_class VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_ny_water_qualities UNIQUE (name, basin, description, water_quality_class, waterbody_class)
);


CREATE TABLE IF NOT EXISTS fishes(
    id SERIAL PRIMARY KEY,
    waterbody_id SMALLINT NOT NULL,
    date_id SMALLINT NOT NULL,
    species_name VARCHAR(255) NOT NULL,
    size_inches DECIMAL NOT NULL,
    number INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_fishes UNIQUE (waterbody_id, date_id, species_name, size_inches, number)
);
CREATE INDEX IF NOT EXISTS fish_species_index ON fishes (species_name);


CREATE TABLE IF NOT EXISTS waterbodies(
    id SERIAL PRIMARY KEY,
    waterbody_name VARCHAR(255),
    waterbody_class VARCHAR(255),
    description VARCHAR(255),
    basin_name VARCHAR(255),
    water_quality_class VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_waterbodies UNIQUE (waterbody_name, waterbody_class, description, basin_name, water_quality_class)
);


CREATE TABLE IF NOT EXISTS dates(
    id SERIAL PRIMARY KEY,
    month VARCHAR(255) NOT NULL,
    year INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_dates UNIQUE (month, year)
);



