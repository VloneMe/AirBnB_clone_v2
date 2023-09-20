-- This script prepares a MySQL server for the project:

-- This creates A database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- This creates or update the user 'hbnb_dev' with the password 'hbnb_dev_pwd'
-- The identified by clause specifies the password.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- This Grant all privileges on the 'hbnb_dev_db' database to 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- A Grant SELECT privilege on the 'performance_schema' database to 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
