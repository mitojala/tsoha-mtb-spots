CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE spots (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
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

CREATE TABLE spot_comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    spot_id INTEGER REFERENCES spots,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);