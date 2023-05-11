CREATE DATABASE studybuddies;
-- This table holds all the characteristics for the user. All the user's information is stored.
CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        major VARCHAR(255)  DEFAULT 'No major',
        first_name VARCHAR(255)  DEFAULT 'No first',
        last_name VARCHAR(255)  DEFAULT 'No last',
        major_changed_count INTEGER DEFAULT 0

    );

CREATE TABLE compsci (
        post_id SERIAL PRIMARY KEY,
        username VARCHAR(255)  NOT NULL,
        useremail VARCHAR(255)  NOT NULL,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER DEFAULT 0,
        message_dislikes INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE post_likes_compsci (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        post_id INTEGER REFERENCES compsci(post_id),
        rating VARCHAR(255)  DEFAULT 'unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );



-- This is the table for the Biology majors
CREATE TABLE biology (
        post_id SERIAL PRIMARY KEY,
        username VARCHAR(255)  NOT NULL,
        useremail VARCHAR(255)  NOT NULL,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER DEFAULT 0,
        message_dislikes INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE post_likes_biology (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        post_id INTEGER REFERENCES biology(post_id),
        rating VARCHAR(255)  DEFAULT 'unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );

-- This is the table for the Business majors
CREATE TABLE business (
        post_id SERIAL PRIMARY KEY,
        username VARCHAR(255)  NOT NULL,
        useremail VARCHAR(255)  NOT NULL,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER DEFAULT 0,
        message_dislikes INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE post_likes_business (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        post_id INTEGER REFERENCES business(post_id),
        rating VARCHAR(255)  DEFAULT 'unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );
-- This is the table for the Engineering majors
CREATE TABLE engineering (
        post_id SERIAL PRIMARY KEY,
        username VARCHAR(255)  NOT NULL,
        useremail VARCHAR(255)  NOT NULL,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER DEFAULT 0,
        message_dislikes INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE post_likes_engineer (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        post_id INTEGER REFERENCES engineering(post_id),
        rating VARCHAR(255)  DEFAULT 'unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );

CREATE TABLE generalform (
        post_id SERIAL PRIMARY KEY,
        username VARCHAR(255)  NOT NULL,
        useremail VARCHAR(255)  NOT NULL,
        forum_message VARCHAR(255) NOT NULL,
        message_likes INTEGER DEFAULT 0,
        message_dislikes INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE post_likes_general (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        post_id INTEGER REFERENCES generalform(post_id),
        rating VARCHAR(255)  DEFAULT 'unknown',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );