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
    latitude DECIMAL,
    longitude DECIMAL,
    sent_at TIMESTAMP
);