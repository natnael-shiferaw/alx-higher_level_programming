-- Create the table 'unique_id' on your MySQL server with a unique constraint on the 'id' column and a default value
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
