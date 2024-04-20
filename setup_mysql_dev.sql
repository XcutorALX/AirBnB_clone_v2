-- This script sets up the MySQL database for the development environment.
-- It creates the database, the user, and the tables.
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
USE `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_Schema.* TO 'hbnb_dev'@'localhost';