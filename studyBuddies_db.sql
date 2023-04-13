CREATE DATABASE studybuddies;
CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        major VARCHAR(255)  DEFAULT 'No major',
        first_name VARCHAR(255)  DEFAULT 'No first',
        last_name VARCHAR(255)  DEFAULT 'No last'
    );
-- This is table for Computer Science majors
CREATE TABLE compSci (
        post_id INTEGER PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )
-- This is the table for the Biology majors
CREATE TABLE biology (
        post_id INTEGER PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )
-- This is the table for the Business majors
CREATE TABLE business (
        post_id INTEGER PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )
-- This is the table for the Engineering majors
CREATE TABLE engineering (
        post_id INTEGER PRIMARY KEY,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER,
        major_id VARCHAR(255)
    )