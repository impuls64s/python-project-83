CREATE TABLE urls (
    id serial PRIMARY KEY,
    name varchar(255) UNIQUE NOT NULL,
    created_at timestamp NOT NULL
);

CREATE TABLE url_checks (
    id serial PRIMARY KEY,
    url_id bigint REFERENCES urls(id) NOT NULL,
    status_code int,
    h1 varchar(255),
    title varchar(255),
    description text,
    created_at timestamp NOT NULL
);

CREATE TABLE all_site (
    id serial PRIMARY KEY,
    urls_name varchar(255) REFERENCES urls(name) NOT NULL,
    last_check  timestamp,
    status_code int
);
