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

-- This is a table for the computer science major. 
CREATE TABLE compSci (
        post_id INTEGER PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    );

-- Table for general form page
CREATE TABLE post (
        id SERIAL PRIMARY KEY,
        content TEXT,
        user_id INTEGER REFERENCES users(id),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
