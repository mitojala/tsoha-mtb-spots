CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE spots (
    id SERIAL PRIMARY KEY,
    name TEXT,
    type TEXT,
    description TEXT,
    sent_at TIMESTAMP
);