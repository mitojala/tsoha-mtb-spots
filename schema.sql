CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE spots (
    id SERIAL PRIMARY KEY,
    name TEXT,
    spot_type TEXT,
    description TEXT,
    difficulty INTEGER,
    latitude DECIMAL,
    longitude DECIMAL,
    sent_at TIMESTAMP,
    has_image BOOLEAN,
    visible BOOLEAN
);

CREATE TABLE spot_images (
    id SERIAL PRIMARY KEY,
    spot_id INTEGER REFERENCES spots,
    spot_image BYTEA
);