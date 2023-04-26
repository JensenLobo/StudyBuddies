CREATE DATABASE studybuddies;
-- This table holds all the characteristics for the user. All the user's information is stored.
CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        major VARCHAR(255)  DEFAULT 'No major',
        first_name VARCHAR(255)  DEFAULT 'No first',
        last_name VARCHAR(255)  DEFAULT 'No last'
    );

CREATE TABLE compSci (
        post_id SERIAL PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    );

-- Table for general form page
CREATE TABLE post (
        id SERIAL PRIMARY KEY,
        user_name varchar(255),
        content TEXT,
        user_id INTEGER REFERENCES users(id),
        message_likes INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );

-- This is the table for the Biology majors
CREATE TABLE biology (
        post_id SERIAL PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )
-- This is the table for the Business majors
CREATE TABLE business (
        post_id SERIAL PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )
-- This is the table for the Engineering majors
CREATE TABLE engineering (
        post_id SERIAL PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )