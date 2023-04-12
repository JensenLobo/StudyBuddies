    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        major VARCHAR(255)  DEFAULT 'No major',
        first_name VARCHAR(255)  DEFAULT 'No first',
        last_name VARCHAR(255)  DEFAULT 'No last'
        
        
    );
