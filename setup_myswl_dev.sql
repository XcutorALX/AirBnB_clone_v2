-- This script sets up the MySQL database for the development environment.
-- Create the database 
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- Uses the database
-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Flush the privileges
FLUSH PRIVILEGES;
-- Grant select on performance schema
GRANT SELECT ON performance_Schema.* TO 'hbnb_dev'@'localhost';
-- Flush the privileges
FLUSH PRIVILEGES;