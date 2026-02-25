CREATE DATABASE IF NOT EXIST clean_database;

CREATE TABLE IF NOT EXISTS 'clean_database'.'users' (
    id BIGINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    age BIGINt NOT NULL,
    PRIMARY KEY(id)
);

