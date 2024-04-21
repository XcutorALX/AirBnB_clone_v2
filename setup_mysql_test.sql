-- Create a database and user for testing
-- Creates a database named hbnb_test_Db
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- Creates a user named `hbnb_test`
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privileges on the database hbnb_test_db to the user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants SELECT on the database performance_Schema to the user hbnb_test
GRANT SELECT ON performance_Schema.* TO 'hbnb_test'@'localhost';
