-- This script prepares a MySQL server for the project:

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update the user 'hbnb_test' with the password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- This grant all privileges on the 'hbnb_test_db' database to 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- This grant SELECT privilege on the 'performance_schema' database to 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
