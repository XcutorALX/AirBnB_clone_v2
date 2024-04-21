-- This script sets up the MySQL database for the development environment.
-- Creates a database named hbnb_dev_Db
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
-- Creates a table named `hbnb_dev`
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privileges on the database hbnd_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Flushes the privileges
FLUSH PRIVILEGES;
-- Grants SELECT on the database performance_Schema to the user hbnb_dev
GRANT SELECT ON performance_Schema.* TO 'hbnb_dev'@'localhost';
-- Flushes the privileges
FLUSH PRIVILEGES;